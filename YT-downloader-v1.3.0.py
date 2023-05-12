import tkinter as tk
from pytube import YouTube
from tkinter import messagebox, filedialog

# Function to download the video
def download():
    try:
        # Get the video URL from the input field
        url = url_entry.get()

        # Check if the user selected a download directory
        if download_dir.get() == "":
            messagebox.showerror("One more thang...", "Please select a download directory!")
            return

        # Create a YouTube object and get the highest resolution stream
        video = YouTube(url, use_oauth=True, allow_oauth_cache=True).streams.get_highest_resolution()

        # Get the filename and extension
        filename = video.default_filename
        ext = filename.split(".")[-1]

        # Check if the user wants to download audio-only
        if download_audio_only.get() == 1:
            # Select the highest bitrate audio stream
            audio = YouTube(url, use_oauth=True, allow_oauth_cache=True).streams.get_audio_only()
            # Set the filename and extension to the audio stream's
            filename = audio.default_filename
            ext = filename.split(".")[-1]
            # Download the audio stream to the selected directory
            audio.download(download_dir.get(), filename=filename)
            messagebox.showinfo("You did it!", "Audio downloaded successfully!")
        else:
            # Download the video to the selected directory
            video.download(download_dir.get(), filename=filename)
            messagebox.showinfo("You did it!", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Fix the URL!", str(e))

# Function to select the download directory
def select_dir():
    download_dir.set(filedialog.askdirectory())

# Create the main window
root = tk.Tk()

# Set the window title
root.title("BrettSports YouTube Downloader")

# Create a label and an entry field for the video URL
url_label = tk.Label(root, text="Enter the video URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a label and an entry field for the download directory
dir_label = tk.Label(root, text="Select download directory:")
dir_label.grid(row=1, column=0, padx=5, pady=5)
download_dir = tk.StringVar()
dir_entry = tk.Entry(root, width=50, textvariable=download_dir)
dir_entry.grid(row=1, column=1, padx=5, pady=5)
dir_button = tk.Button(root, text="Browse", command=select_dir)
dir_button.grid(row=1, column=2, padx=5, pady=5)

# Create a checkbox for audio-only download
download_audio_only = tk.IntVar()
audio_check = tk.Checkbutton(root, text="Audio-only", variable=download_audio_only)
audio_check.grid(row=2, column=1, padx=5, pady=5)

# Create a button to start the download
download_button = tk.Button(root, text="Download", command=download)
download_button.grid(row=3, column=1, padx=5, pady=5)

# Run the main loop
root.mainloop()
