from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")

Label(root,text = 'YouTube Video Downloader', font = 'arial 20 bold').pack()
link = StringVar()

Label(root,text = 'Paste Link Here:',font = 'arial 15 bold').place(x=160, y=68)
link_enter = Entry(root, width = 70,textvariable = link).place(x=32, y=90)
def Downloader():
    url=YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font = 'arial 15').place(x=100,y=210)

Button(root,text = 'DOWNLOAD',font = 'arial 15 bold' ,
       bg='pale violet red', padx=2, command=Downloader).place(x=180, y=150)

root.mainloop()