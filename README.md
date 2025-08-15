# Episode Downloader

A Python script that automatically downloads video episodes from `.m3u8` streams found in webpage network traffic using Selenium and `ffmpeg`.

## Features
- Parses episode titles from the URL and saves them with clean filenames
- Automatically increments to the next episode based on the URL pattern (e.g., `S01E01` → `S01E02`)
- Retries download if the `.m3u8` link isn’t found immediately
- Headless Chrome for faster execution

---

## Requirements

### 1. Install Python
Python **3.8+** is recommended.

### 2. Install Dependencies
```bash
pip install selenium selenium-wire

### 3. Install Google Chrome
Download from https://www.google.com/chrome/
Make sure the chrome.exe path in the script matches your installation:
```bash
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

### 4. Install FFmpeg
Download from https://ffmpeg.org/download.html and make sure it’s added to your system’s PATH.

###How to Run
