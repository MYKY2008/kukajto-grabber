import subprocess
import time
import os
import re
from urllib.parse import urlparse
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name)


def parse_filename_from_url(url):
    path_parts = urlparse(url).path.strip("/").split("/")
    if len(path_parts) >= 2:
        show_raw = path_parts[-2]
        episode_raw = path_parts[-1]
        show_name = " ".join(word.capitalize() for word in show_raw.split("-"))
        episode_name = re.sub(r'(S\d{2})E(\d{2})', r'\1 E\2', episode_raw, flags=re.IGNORECASE)
        return f"{show_name} {episode_name}"
    else:
        return "video"


def increment_episode_url(url):
    match = re.search(r'(S\d{2}E)(\d{2})', url, re.IGNORECASE)
    if match:
        prefix, num = match.groups()
        next_num = int(num) + 1
        return url.replace(match.group(0), f"{prefix}{next_num:02d}")
    return None


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.scopes = ['.*']
    return driver


def download_episode(episode_url, output_path, retries=3):
    for attempt in range(1, retries + 1):
        driver = create_driver()
        time.sleep(1)
        driver.get(episode_url)
        print(f"[Attempt {attempt}] Processing {episode_url} ...")

        # Detect redirection to main page
        parsed_url = urlparse(episode_url)
        main_page_url = f"{parsed_url.scheme}://{parsed_url.netloc}/{parsed_url.path.strip('/').split('/')[0]}"
        time.sleep(5)  # wait for possible redirect
        if driver.current_url.rstrip("/") == main_page_url.rstrip("/"):
            print("⚠ Reached series main page — no more episodes.")
            driver.quit()
            return False

        # Try clicking play
        try:
            video_element = driver.find_element(By.TAG_NAME, "video")
            ActionChains(driver).move_to_element(video_element).click().perform()
        except Exception:
            pass

        found_link = None
        start_time = time.time()
        timeout = 60

        while time.time() - start_time < timeout and not found_link:
            for request in driver.requests:
                if request.response and ".m3u8" in request.url:
                    found_link = request.url
                    print(f"Found m3u8: {found_link}")
                    break
            time.sleep(1)

        driver.quit()

        if found_link:
            cmd = [
                "ffmpeg", "-i", found_link,
                "-c", "copy", "-bsf:a", "aac_adtstoasc",
                output_path
            ]
            try:
                subprocess.run(cmd, check=True)
                print(f"✅ Download complete: {output_path}")
                return True
            except subprocess.CalledProcessError as e:
                print("❌ Error downloading video:", e)
        else:
            print("⚠ No .m3u8 link found — retrying...")

        print("Restarting Chrome and retrying...")

    print(f"❌ Failed to download {episode_url} after {retries} attempts.")
    return False


def main():
    episode_url = input("Enter first episode URL: ").strip()

    while True:
        filename = sanitize_filename(parse_filename_from_url(episode_url)) + ".mp4"
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", filename)

        success = download_episode(episode_url, desktop_path)
        if not success:
            break

        time.sleep(3)
        episode_url = increment_episode_url(episode_url)
        if not episode_url:
            break

    print("All available episodes processed!")


if __name__ == "__main__":
    main()
