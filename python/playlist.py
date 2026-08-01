
import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import Playlist
import os

def download_playlist(url, save_path):
    try:
        playlist = Playlist(url)
        if not playlist:
            raise Exception("Invalid playlist URL")

        if not save_path:
            save_path = "./Downloaded_Playlist"
        
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        for video in playlist.videos:
            try:
                stream = video.streams.get_highest_resolution()
                video_title = stream.title
                stream.download(save_path)
                print(f"Downloaded: {video_title}")
            except Exception as e:
                print(f"Error downloading {video.title}: {e}")
        
        messagebox.showinfo("Success", "Playlist downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download playlist: {e}")

def on_browse_click():
    global save_path
    save_path = filedialog.askdirectory()
    if save_path:
        location_label.config(text=f"Download Location: {save_path}")

def on_download_click():
    playlist_url = url_entry.get()
    if playlist_url:
        if 'save_path' in globals():
            download_playlist(playlist_url, save_path)
        else:
            messagebox.showwarning("Input Error", "Please select a download location")
    else:
        messagebox.showwarning("Input Error", "Please enter a playlist URL")

# Create the GUI application
root = tk.Tk()
root.title("YouTube Playlist Downloader")
root.geometry("720x480")

# Center the window
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth()/2 - window_width/2)
position_down = int(root.winfo_screenheight()/2 - window_height/2)
root.geometry("+{}+{}".format(position_right, position_down))

# URL input
tk.Label(root, text="Playlist URL:", anchor="center").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Download location
browse_button = tk.Button(root, text="Browse", command=on_browse_click, bg="blue", fg="white")
browse_button.pack(pady=10)
location_label = tk.Label(root, text="No location selected")
location_label.pack()

# Download button
download_button = tk.Button(root, text="Download", command=on_download_click, bg="blue", fg="white")
download_button.pack(pady=10)

root.mainloop()