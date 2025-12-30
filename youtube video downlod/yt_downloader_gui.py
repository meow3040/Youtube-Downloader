#!/usr/bin/env python3
"""
YouTube Video Downloader with GUI
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from yt_dlp import YoutubeDL
import os


class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("600x550")
        self.root.resizable(False, False)

        self.download_path = os.getcwd()
        self.is_downloading = False

        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="YouTube Video Downloader",
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=20)

        # URL Input
        url_frame = tk.Frame(self.root)
        url_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(url_frame, text="Video URL:", font=("Arial", 10)).pack(anchor="w")
        self.url_entry = tk.Entry(url_frame, font=("Arial", 10))
        self.url_entry.pack(fill="x", pady=5)

        # Quality Selection
        quality_frame = tk.Frame(self.root)
        quality_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(quality_frame, text="Quality:", font=("Arial", 10)).pack(anchor="w")
        self.quality_var = tk.StringVar(value="best")
        quality_options = [
            ("Best Quality", "best"),
            ("1080p", "bestvideo[height<=1080]+bestaudio/best[height<=1080]"),
            ("720p", "bestvideo[height<=720]+bestaudio/best[height<=720]"),
            ("480p", "bestvideo[height<=480]+bestaudio/best[height<=480]"),
            ("Audio Only (MP3)", "bestaudio/best")
        ]

        for text, value in quality_options:
            tk.Radiobutton(
                quality_frame,
                text=text,
                variable=self.quality_var,
                value=value,
                font=("Arial", 9)
            ).pack(anchor="w")

        # Download Path
        path_frame = tk.Frame(self.root)
        path_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(path_frame, text="Download Location:", font=("Arial", 10)).pack(anchor="w")

        path_select_frame = tk.Frame(path_frame)
        path_select_frame.pack(fill="x", pady=5)

        self.path_label = tk.Label(
            path_select_frame,
            text=self.download_path,
            font=("Arial", 9),
            anchor="w",
            bg="white",
            relief="sunken"
        )
        self.path_label.pack(side="left", fill="x", expand=True, padx=(0, 5))

        browse_btn = tk.Button(
            path_select_frame,
            text="Browse",
            command=self.browse_folder,
            font=("Arial", 9)
        )
        browse_btn.pack(side="right")

        # Download Button
        self.download_btn = tk.Button(
            self.root,
            text="Download",
            command=self.start_download,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            height=2
        )
        self.download_btn.pack(pady=20)

        # Status Label
        self.status_label = tk.Label(
            self.root,
            text="Ready",
            font=("Arial", 10),
            fg="blue"
        )
        self.status_label.pack(pady=5)

        # Progress Bar
        self.progress = ttk.Progressbar(
            self.root,
            mode='indeterminate',
            length=400
        )
        self.progress.pack(pady=10)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.download_path = folder
            self.path_label.config(text=folder)

    def update_status(self, message, color="blue"):
        self.status_label.config(text=message, fg=color)

    def start_download(self):
        url = self.url_entry.get().strip()

        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return

        if self.is_downloading:
            messagebox.showwarning("Warning", "A download is already in progress")
            return

        # Start download in a separate thread
        thread = threading.Thread(target=self.download_video, args=(url,))
        thread.daemon = True
        thread.start()

    def download_video(self, url):
        self.is_downloading = True
        self.download_btn.config(state="disabled", bg="gray")
        self.progress.start()
        self.update_status("Downloading...", "orange")

        try:
            quality = self.quality_var.get()

            # Configure yt-dlp options
            ydl_opts = {
                'format': quality,
                'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
            }

            # If audio only, convert to MP3
            if quality == "bestaudio/best":
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.update_status("Download completed successfully!", "green")
            messagebox.showinfo("Success", "Video downloaded successfully!")

        except Exception as e:
            self.update_status(f"Error: {str(e)}", "red")
            messagebox.showerror("Error", f"Download failed:\n{str(e)}")

        finally:
            self.is_downloading = False
            self.progress.stop()
            self.download_btn.config(state="normal", bg="#4CAF50")


def main():
    root = tk.Tk()
    app = YouTubeDownloaderGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
