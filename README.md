# Episode Downloader

A Python script that automatically downloads video episodes from `.m3u8` streams found in webpage network traffic using Selenium and `ffmpeg`.

## Features
- Parses episode titles from the URL and saves them with clean filenames
- Automatically increments to the next episode based on the URL pattern (e.g., `S01E01` → `S01E02`)
- Retries download if the `.m3u8` link isn’t found immediately
- Headless Chrome for faster execution

---

## Requirements

### 1) Install Python
Python **3.8+** is recommended. Verify with:
```bash
python --version
```

### 2) Install Dependencies
Install Selenium and Selenium Wire:
```bash
pip install selenium selenium-wire
```

### 3) Install Google Chrome
Download from: <https://www.google.com/chrome/>

Make sure the Chrome binary path in the script matches your installation (Windows default shown):
```python
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
```
**macOS** (usually you can omit the `binary_location`; if needed, use):
```python
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```
**Linux** (usually you can omit the `binary_location`; if needed, use):
```python
chrome_options.binary_location = "/usr/bin/google-chrome"
```

### 4) Install ChromeDriver
- Download from: <https://chromedriver.chromium.org/downloads>
- Ensure the **ChromeDriver version matches your Chrome version**.
- Put `chromedriver` somewhere on your system `PATH` **or** specify the path explicitly in the script:
```python
from selenium.webdriver.chrome.service import Service
webdriver.Chrome(service=Service("path/to/chromedriver"), options=chrome_options)
```
Verify installation:
```bash
chromedriver --version
```

### 5) Install FFmpeg
Download from: <https://ffmpeg.org/download.html> and ensure `ffmpeg` is on your system `PATH`.

Verify installation:
```bash
ffmpeg -version
```

---

## Quick Start

1. Save the script as `episode_downloader.py`.
2. Open a terminal in the script’s folder.
3. Run:
```bash
python episode_downloader.py
```
4. When prompted, paste the URL of the **first episode** (must contain `SxxExx` in the URL, e.g., `S01E01`).
5. The script will:
   - Detect the `.m3u8` stream from network requests.
   - Download the current episode to your **Desktop** with a cleaned filename.
   - Increment the episode number (e.g., `S01E01` → `S01E02`) and attempt the next one.
   - Stop automatically when it reaches the series main page or fails to find the next episode.

---

## Usage Details

- **URL pattern required:** The episode URL must include `SxxExx` (e.g., `.../show-name/S01E03`).  
- **Output filename:** Derived from the URL; example: `Show Name S01 E03.mp4` saved to your Desktop.
- **Retries:** Each episode download will retry up to **3** times if no `.m3u8` is found (configurable in `download_episode(..., retries=3)`).
- **Timeout:** The script listens for network requests up to **60 seconds** per attempt. You can increase this by changing `timeout` in the code.
- **Headless mode:** Enabled by default via `--headless=new` for speed. You can remove this flag if the site blocks headless browsers.

---

## Example Run
```text
Enter first episode URL: https://example.com/show-name/S01E01
[Attempt 1] Processing https://example.com/show-name/S01E01 ...
Found m3u8: https://examplecdn.com/streams/12345/master.m3u8
✅ Download complete: C:\Users\Username\Desktop\Show Name S01 E01.mp4
[Attempt 1] Processing https://example.com/show-name/S01E02 ...
Found m3u8: https://examplecdn.com/streams/12346/master.m3u8
✅ Download complete: C:\Users\Username\Desktop\Show Name S01 E02.mp4
⚠ Reached series main page — no more episodes.
All available episodes processed!
```

---

## Troubleshooting

- **No `.m3u8` link found — retrying...**
  - Some sites delay video initialization. Increase the `timeout` or try removing headless mode.
- **Version mismatch / Chrome failed to start**
  - Ensure ChromeDriver **matches** your installed Chrome version.
- **`ffmpeg` not found**
  - Add FFmpeg to your system `PATH` and verify with `ffmpeg -version`.
- **Blocked in headless mode**
  - Remove the `--headless=new` argument in `create_driver()` to see the browser UI.
- **Permission errors on Windows**
  - Run the terminal as Administrator if ChromeDriver needs elevated permissions or choose a writable temp directory.

---

## Notes & Legal
- Works only for sites where episode URLs contain a pattern like `/show-name/S01E01`.
- Designed for **personal/offline use** cases. **Only download content that you own or have the rights to download.** You are responsible for complying with site terms and applicable laws.
- Behavior can vary by site; some may use additional protections that prevent automated downloading.

---

## Script Entry Point
Your script already includes:
```python
if __name__ == "__main__":
    main()
```
So running `python episode_downloader.py` in the script directory will start the tool and prompt for the first episode URL.
