# Kukajto Episode Downloader

A Python script that automatically downloads video episodes from .m3u8 streams found in webpage network traffic using Selenium and ffmpeg.

Features

Parses episode titles from the URL and saves them with clean filenames

Automatically increments to the next episode based on the URL pattern (e.g., S01E01 → S01E02)

Retries download if the .m3u8 link isn’t found immediately

Headless Chrome for faster execution
