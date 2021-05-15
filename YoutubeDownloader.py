from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import time
from progress.bar import Bar
from pytube import YouTube

root = Tk()

frame = Frame(root)
frame.pack(padx=10, pady=10)

text = Text(frame)
text = StringVar()
label = Label(frame, text="Download Link", font=('bold', 14))
label.pack()
entry = Entry(frame, textvariable=text, width=50)
entry.pack(pady=10)
txt = Label(frame, text='0%', font=('bold', 14))
txt.pack()
Label(root, text="Powered by @OgabekYuldoshev").pack(side=BOTTOM)


def onDownloadVideo():
    if entry.get().replace(" ", "") == "" :
        messagebox.showerror("Error", "Pleas, Fill in required fields correctly")
    else :
        yt = YouTube(entry.get())
        Label(root, text=yt.title, font=('bold', 10), wraplength=400).pack()
        bar = Bar('Downloading', max=100)
        entry.config(state='disabled')
        buttonVideo.config(state='disabled')
        buttonMusic.config(state='disabled')
        counter = 0
        for i in range(100):
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
            counter += 1
            txt['text']= counter,'%'
            root.update()
            bar.next()
        bar.finish()
        entry.config(state='normal')
        buttonVideo.config(state='normal')
        buttonMusic.config(state='normal')
        messagebox.showinfo("Successfully", "Your video is downloaded!!!")

def onDownloadMusic():
    if entry.get().replace(" ", "") == "" :
        messagebox.showerror("Error", "Pleas, Fill in required fields correctly")
    else :
        yt = YouTube(entry.get())
        Label(root, text=yt.title, font=('bold', 10), wraplength=400).pack()
        bar = Bar('Downloading', max=100)
        entry.config(state='disabled')
        buttonVideo.config(state='disabled')
        buttonMusic.config(state='disabled')

        counter = 0
        for i in range(100):
            yt.streams.filter(only_audio=True).first().download()
            counter += 1
            txt['text']= counter,'%'
            root.update()
            bar.next()
        bar.finish()
        entry.config(state='normal')
        buttonVideo.config(state='normal')
        buttonMusic.config(state='normal')
        messagebox.showinfo("Successfully", "Your music is downloaded!!!")




buttonVideo = Button(frame, command=onDownloadVideo, text="Download Video", padx=3)
buttonMusic = Button(frame, command=onDownloadMusic, text="Download Music", padx=3)

buttonVideo.pack(side=LEFT)
buttonMusic.pack(side=RIGHT)

root.iconbitmap("icon.ico")

root.title('Youtube Downloader')
screenH = root.winfo_screenheight()
screenW = root.winfo_screenwidth()
x = (screenW / 2) - (500 / 2)
y = (screenH / 2) - (200 / 2)
root.geometry(f'{500}x{200}+{int(x)}+{int(y)}')
root.mainloop()
