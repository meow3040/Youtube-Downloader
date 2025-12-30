# YouTube Video Downloader

A simple and user-friendly GUI application for downloading YouTube videos in various quality formats.

## Features

- Clean and intuitive graphical interface
- Multiple quality options:
  - Best Quality
  - 1080p
  - 720p
  - 480p
  - Audio Only (MP3)
- Custom download location selection
- Real-time download status updates
- Progress indicator
- Audio extraction to MP3 format

## Requirements

- Python 3.x
- yt-dlp

## Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. For audio conversion to MP3, you'll need FFmpeg installed on your system:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` (Debian/Ubuntu) or `sudo yum install ffmpeg` (RedHat/CentOS)

## Usage

Run the application:

```bash
python yt_downloader_gui.py
```

1. Paste a YouTube video URL into the input field
2. Select your desired quality
3. Choose a download location (optional, defaults to current directory)
4. Click the "Download" button
5. Wait for the download to complete

## Notes

- The application uses yt-dlp for downloading, which supports YouTube and many other video platforms
- Downloaded videos will be saved with their original title
- Audio-only downloads are automatically converted to MP3 format
- Only one download can be active at a time

## License

This project is provided as-is for educational purposes.
