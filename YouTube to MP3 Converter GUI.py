from pytube import YouTube
import os
import tkinter as tk
from tkinter import messagebox

def Download():
    #Parsing YouTube link and local machine destination passed down from GUI
    ytlink = entry.get()
    print(ytlink)
    dest = destination_entry.get()
    print(dest)

    #Start downloading the audio stream via the YouTube link and download it to destination specified by user
    yt=YouTube(ytlink)
    audio = yt.streams.filter(only_audio=True).__getitem__(1)
    downloaded_file = audio.download(output_path=dest)

    #File grabbed from pytube stream will be in mp4 format, hard convert to mp3
    filename, file_extension = os.path.splitext(downloaded_file)
    mp3file = filename + '.mp3'
    os.rename(downloaded_file, mp3file)

    messagebox.showinfo("Success", "Your song is downloaded")
    
window = tk.Tk()
window.geometry("400x350")
window.title("Youtube to MP3 Converter")

#Text and textbox prompting user to enter youtube link to convert
download_prompt = tk.Label(window, text="Enter the link you wish to convert")
download_prompt.pack()
entry = tk.Entry(window, width=50)
entry.pack()


#Text and textbox prompting user to enter where to save on their pc
destination_prompt = tk.Label(window, text="Enter the destination you wish to save your file to")
destination_prompt.pack()
destination_entry = tk.Entry(window, width=50)
destination_entry.pack()


#button to activate the download process
button = tk.Button(
    text="Download",
    width=25,
    height=2,
    command=Download
)
button.pack()

window.mainloop()
