import tkinter as tk

window = tk.Tk()
window.geometry("400x350")
window.title("Youtube to MP3 Converter")

download_prompt = tk.Label(text="Enter the link you wish to convert")
download_prompt.pack()
entry = tk.Entry(width=50)
entry.pack()
link = entry.get()

button = tk.Button(
    text="Download",
    width=25,
    height=2,
    command=lambda: Download(link)
)
button.pack()
window.mainloop()
