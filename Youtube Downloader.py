from tkinter import*
from pytube import YouTube

root = Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title("Youtube Downloader")

Label(root, text="Youtube Downloader", fg="red", font="arial 20 bold").pack(pady=9)

link = StringVar()
Label(root, text="Past Link Here", font="arial 15 bold").place(x= 170 , y= 45)
link_here = Entry(root, width=1000000 ,textvariable=link).place(x= 0, y=80)

def high():
    url = YouTube(str(link.get()))
    video =url.streams.get_highest_resolution()
    video.download()
    Label(root, text="Downloaded!", fg="black", font="arial 15 bold").place(x=100, y=80)
Button(root, text="Download high reslution",bg="green", font="arial 15 bold", command=high).place(x=252, y=100)
def low():
    url = YouTube(str(link.get()))
    video =url.streams.get_lowest_resolution()
    video.download()
    Label(root, text="Downloaded!", fg="black", font="arial 15 bold").place(x=100, y=80)
Button(root, text="Download low reslution",fg="black", font="arial 15 bold", command=low).place(x=0, y=100)

def audio_only():
    url = YouTube(str(link.get()))
    video =url.streams.get_audio_only()
    video.download()
    Label(root, text="Downloaded!", fg="black", font="arial 15 bold").place(x=100, y=80)
Button(root, text="Download audio only",bg="light yellow", font="arial 15 bold", command=audio_only).place(x=140,y=150)

root.mainloop()