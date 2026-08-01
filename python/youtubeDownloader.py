import pytube
import customtkinter
import tkinter
from tkinter import filedialog

# Function to download the video
def Download(): 
    try:
        ytlink = link.get()
        ytObject = pytube.YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if not video:
            finishlabel.configure(text="No video available", text_color="red")
            return
        title.configure(text=ytObject.title, text_color="green")
        finishlabel.configure(text="")
        download_path = path.get()
        video.download(output_path=download_path)
        finishlabel.configure(text="Video Downloaded!")
    except Exception as e:
        finishlabel.configure(text="Youtube link is invalid", text_color="red")
        print(e)

# Progress callback function
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytesDownloaded = total_size - bytes_remaining
    percentage_of_completion = bytesDownloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progress.configure(text=per + '%')
    progress.update()
    progressBar.set(float(percentage_of_completion) / 100)

# Function to set the download location
def set_location():
    download_path = filedialog.askdirectory()
    path.set(download_path)

# Initialize customtkinter appearance
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Create the main app window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Title label
title = customtkinter.CTkLabel(app, text="Insert Your video URL")
title.pack(padx=10, pady=10)

# Entry for YouTube link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Label to display download status
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

# Progress label
progress = customtkinter.CTkLabel(app, text="0%")
progress.pack()

# Progress bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Button to start download
download = customtkinter.CTkButton(app, text="Download", command=Download)
download.pack(padx=10, pady=10)

# Path variable and button to set download location
path = tkinter.StringVar()
location_button = customtkinter.CTkButton(app, text="Set Download Location", command=set_location)
location_button.pack(padx=10, pady=10)

# Run the application
app.mainloop()
