def download_best_mp3():
    
    #下載mp4
    dest =f'./download'
    video = YouTube(input_url.get())
    print(video.streams)
    bestAbrVideo = video.streams.filter(only_audio=True).order_by("abr").desc().first()
    out_file = bestAbrVideo.download(output_path=dest)

    #mp4 換 mp3
    filename,ext = os.path.splitext(out_file)
    new_file = filename + '.mp3'
    try:
        os.rename(out_file,new_file)
    except:
        display_box.config(text="檔案已存在")
        return
    #顯示完成Message
    display_box.config(text=video.title+" download Complete")

def download_best_video():
    
    # #下載mp4
    dest =f'./download'
    yt = YouTube(input_url.get())
    display_box.config(text="Video is download...")
    spac = ""
    try:
        # 下載 視訊與音訊 因Dash規範最高只到720p，所以要自己合成。
        print(yt.streams.filter(res="1080p").first())
        yt.streams.filter(res="1080p").order_by("fps").desc().first().download(filename="video.mp4")
        print(yt.streams.filter(only_audio=True,mime_type="audio/mp4").order_by("abr").desc().first())
        yt.streams.filter(only_audio=True).order_by("abr").desc().first().download(filename="audio.mp4")
        
        #去除格式的特殊字元，以方便存入
        spac =yt.title.replace("'","").replace("/","")
        audio = ffmpeg.input("audio.mp4")
        video = ffmpeg.input("video.mp4")
        ffmpeg.output(audio, video, "{}.mp4".format(spac)).run()
        display_box.config(text=yt.title+" download Complete")
    except Exception:
        display_box.config(text="download ERROR")
    
import tkinter as tk    
from pytube import YouTube
import xml.etree.ElementTree as ET
import os
from ttkbootstrap import Style
from tkinter import ttk
import ffmpeg
import subprocess  

target_path = "./Downloads"

# window=tk.Tk()
style=Style(theme="darkly")
window=style.master
window.geometry("600x400")
window.title('簡易Youtube影片下載器')

getvideo=""
strftype=""
listvideo=[]#影片格式串列
listradio=[]
itag=0
video=tk.IntVar()
input_url=tk.StringVar()
path=tk.StringVar()
filename=tk.StringVar()

frame=tk.Frame(window,width=450)
frame.pack()
label=ttk.Label(frame,text="Youtube網址：",font=("Arial",16))
label.pack(pady=10)
entryUrl=tk.Entry(frame,textvariable=input_url)
entryUrl.config(width=40)
entryUrl.pack()
btn=ttk.Button(frame,text="下載音訊",style="success.TButton",command=download_best_mp3)
btn.pack()
btnV=ttk.Button(frame,text="下載視訊",style="success.TButton",command=download_best_video)
btnV.pack()
display_box = ttk.Label(frame, text="")
display_box.pack()

window.mainloop()