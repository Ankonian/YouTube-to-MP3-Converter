from pytube import YouTube
import os
import tkinter as tk


#Ask user for the YouTube link
link = str(input("Enter the URL of the video you wish to convert:\n"))
yt=YouTube(link)

#Grab the second audio only stream(highest bitrate mp4 format)
audio = yt.streams.filter(only_audio=True).__getitem__(1)

#Ask user where to save the mp3 file
destination = str(input("Enter the output path, leave blank for current directory:\n")) or '.'
downloaded_file = audio.download(output_path=destination)

#File grabbed from pytube stream will be in mp4 format, hard convert to mp3
filename, file_extension = os.path.splitext(downloaded_file)
mp3file = filename + '.mp3'
os.rename(downloaded_file, mp3file)

#prompting success message 
print(yt.title + " is downloaded successfully")

