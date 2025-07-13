from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Progressbar, Combobox
from pytube import YouTube
import threading

# GUI Window Setup
root = Tk()
root.title("Lalita YouTube Downloader 1.5")
root.geometry("600x350")
root.resizable(False, False)
root.configure(bg="#f8f9fa")

# Global Variables
video_streams = []
yt = None

# Fetch Video Info
def fetch_streams():
    global yt, video_streams
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Missing URL", "Please enter a YouTube video URL.")
        return
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        video_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        if not video_streams:
            raise Exception("No progressive video streams found.")

        # Show available resolutions
        resolutions = [stream.resolution for stream in video_streams]
        quality_menu['values'] = resolutions
        quality_menu.current(0)

        title_label.config(text=f"Title: {yt.title}", fg="blue")
        status_label.config(text="Video found. Choose resolution and download.", fg="green")
    except Exception as e:
        title_label.config(text="")
        status_label.config(text=f"Error: {str(e)}", fg="red")
        messagebox.showerror("Error", f"Could not fetch video.\n{e}\n\n📌 Tip: Run this if error persists:\n\npip install --upgrade pytube")

# Download Thread Starter
def start_download():
    threading.Thread(target=download_video).start()

# Download Video
def download_video():
    try:
        stream = video_streams[quality_menu.current()]
        folder = filedialog.askdirectory()
        if not folder:
            return
        status_label.config(text="Downloading...", fg="orange")
        progress_bar['value'] = 0
        stream.download(output_path=folder)
        status_label.config(text="Download completed!", fg="green")
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        status_label.config(text=f"Download failed: {str(e)}", fg="red")
        messagebox.showerror("Download Error", str(e))

# Progress Callback
def on_progress(stream, chunk, bytes_remaining):
    total = stream.filesize
    downloaded = total - bytes_remaining
    percent = int((downloaded / total) * 100)
    progress_bar['value'] = percent
    root.update_idletasks()

# UI Layout
Label(root, text="🎥 YouTube Video URL:", font=("Arial", 12), bg="#f8f9fa").pack(pady=10)
url_entry = Entry(root, width=60, font=("Arial", 11))
url_entry.pack(pady=2)

Button(root, text="Fetch Video Info", command=fetch_streams, bg="#28a745", fg="white", font=("Arial", 10)).pack(pady=5)

title_label = Label(root, text="", font=("Arial", 11, "bold"), bg="#f8f9fa")
title_label.pack(pady=4)

Label(root, text="Select Resolution:", font=("Arial", 11), bg="#f8f9fa").pack()
quality_menu = Combobox(root, state="readonly", width=15, font=("Arial", 11))
quality_menu.pack(pady=4)

Button(root, text="Download Video", command=start_download, bg="#007bff", fg="white", font=("Arial", 11)).pack(pady=10)

progress_bar = Progressbar(root, length=400, mode='determinate')
progress_bar.pack(pady=10)

status_label = Label(root, text="", font=("Arial", 10), bg="#f8f9fa", fg="black")
status_label.pack()

# Start GUI
root.mainloop()
