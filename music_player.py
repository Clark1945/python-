def choose():
    global playsong
    msg.set("\n播放音樂中:"+choice.get())
    playsong=choice.get()
    
def playmp3():
    global status,playsong,preplaysong
    if playsong==preplaysong:
        if not mixer.music.get_busy(): 
            mixer.music.load(playsong)
            mixer.music.play(loops=-1)
        else:
            mixer.music.unpause()
        msg.set("\n正在播放:{}".format(playsong))
    else:
        playNewmp3()
        preplaysong=playsong
def pausemp3():
    global f
    if (f==True):
        mixer.music.pause()
        msg.set('\n暫停播放{}'.format(playsong))
        f=False
    else:
        mixer.music.unpause()
        f=True
        
def increase():
    global volume
    volume+=0.1
    if volume >=1:
        volume=1
    mixer.music.set_volume(volume)
def decrease():
    global volume
    volume-=0.1
    if volume <=0.1:
        volume=0.1
    mixer.music.set_volume(volume)
def stopmp3():
    mixer.music.stop()
    msg.set("\n停止播放")
def exitmp3():
    mixer.music.stop()
    window.destroy()
def playNewmp3():
    global playsong
    mixer.music.stop()
    mixer.music.load(playsong)
    mixer.music.play(loops=-1)
    msg.set("\n正在播放:{}".format(playsong))
    
    
import tkinter as tk
from pygame import mixer
import glob

mixer.init()
window=tk.Tk()
window.geometry("600x400")
window.title("音樂播放器實作")

labeltitle=tk.Label(window,text="\nmp3 播放器",fg="red",font=("新細明體",12))
labeltitle.pack()
frame1=tk.Frame(window)
frame1.pack()

source_dir="music\mp3\\"
mp3files=glob.glob(source_dir+"*.mp3")

playsong=preplaysong=""
index=0
volume=0.7
f=True
choice=tk.StringVar()

for mp3 in mp3files:
    rbtem=tk.Radiobutton(frame1,text=mp3,variable=choice,value=mp3,command=choose)
    if index==0:
        rbtem.select()
        playsong=preplaysong=mp3
    rbtem.grid(row=index,column=0,sticky="w")
    index+=1
    
msg=tk.StringVar()
msg.set("\n播放歌曲:")
label=tk.Label(window,textvariable=msg,fg="blue",font=("新細明體",10))
label.pack()
labelsep=tk.Label(window,text="\n")
labelsep.pack()

frame2=tk.Frame(window)
frame2.pack()

button1 = tk.Button(frame2,text="播放",width=8,command=playmp3)
button1.grid(row=0,column=0,padx=5,pady=5)

button2 = tk.Button(frame2,text="暫停",width=8,command=pausemp3)
button2.grid(row=0,column=1,padx=5,pady=5)

button3 = tk.Button(frame2,text="調高音量",width=8,command=increase)
button3.grid(row=0,column=2,padx=5,pady=5)

button4 = tk.Button(frame2,text="調低音量",width=8,command=decrease)
button4.grid(row=0,column=3,padx=5,pady=5)

button5 = tk.Button(frame2,text="停止",width=8,command=stopmp3)
button5.grid(row=0,column=4,padx=5,pady=5)

button6 = tk.Button(frame2,text="結束",width=8,command=exitmp3)
button6.grid(row=0,column=5,padx=5,pady=5)

window.protocol("WM_DELETE_WINDOW",exitmp3)

window.mainloop()
