def menu(status):
    os.system("cls")
    print("wav播放器{}".format(status))
    print("------------------------------------------")
    print("1.播放")
    print("2.上一首")
    print("3.下一首")
    print("4.停止")
    print("0.關閉")
    print("------------------------------------------")

def playwav(song):
    global status,sound
    sound=mixer.Sound(wavfiles[index])
    sound.play(loops=0)
    status="Now playing... {}".format(wavfiles[index])
    
def playNewwav(song):
    global status,sound
    sound.stop()
    sound=mixer.Sound(wavfiles[index])
    sound.play(loops=0)
    status="Now playing... {}".format(wavfiles[index])
    
    
from pygame import mixer
import glob,os
mixer.init()
source_dir="music/wav/"
wavfiles=glob.glob(source_dir+"*.wav")
index=0
status=""
print(wavfiles)
sound=mixer.Sound(wavfiles[index])

while True:
    menu(status)
    choice=int(input("選擇！"))
    if choice == 1:
        playwav(wavfiles[index])
        print()
    elif choice==2:
        index+=1
        if index==len(wavfiles):
            index=0
        playNewwav(wavfiles[index])
    elif choice==3:
        index -=1
        if index<0:
            index=len(wavfiles)-1
        playNewwav(wavfiles[index])
    elif choice==4:
        sound.stop()
        status="停止播放"
    else:
        break
sound.stop()
print("執行完畢")
            
        
        