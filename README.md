# Series downloader from kukajto or other sites that uses .m3u8 files to stream the video

A Python script that downloads video episodes from `.m3u8` streams found in webpage network traffic using Selenium Wire and `ffmpeg`.

## Features
- Automatically detects `.m3u8` stream links when playing a video in the browser
- Saves videos with cleaned filenames derived from the episode URL
- Automatically increments the episode number (e.g., S01E01 → S01E02) and downloads the next one
- Stops automatically when there are no more episodes

---

## Requirements

### 1) Install Python
Python **3.8+** is recommended.

Verify installation:
```bash
python --version
```

### 2) Install Dependencies
Install required Python packages:
```bash
pip install selenium-wire
```

### 3) Install Google Chrome
Download from: <https://www.google.com/chrome/>

Make sure the Chrome binary path in the script matches your installation (Windows default shown):
```python
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
```

### 4) Install FFmpeg
Download from: <https://ffmpeg.org/download.html> and ensure it's in your system `PATH`.

Verify installation:
```bash
ffmpeg -version
```

---

## How to Run

1. Save the script as `episode_downloader.py`.
2. Open a terminal in the script’s folder.
3. Run the script:
```bash
python episode_downloader.py
```
4. When prompted, paste the URL of the **first episode** (must contain `SxxExx` in the URL, e.g., `S01E01`).
5. The script will:
   - Play the video in a headless Chrome browser.
   - Detect the `.m3u8` link from network requests.
   - Download the episode using `ffmpeg`.
   - Increment to the next episode URL and repeat until no more episodes are found.

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

## Disclaimer
FOR EDUCATIONAL AND INFORMATIONAL PURPOSES ONLY.

The information provided in or through this website is for educational and informational purposes only and solely as a self-help tool for your own use.

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.

---

## License
This program is released under MIT License.

---

## Notes
- The URL must contain the episode format `SxxExx`.
- Some websites may block headless Chrome; if so, remove `--headless=new` from the script.
