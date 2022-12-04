def clickUrl():  #按「確定」鈕後處理函式
    global listvideo, listradio,yt
    labelMsg.config(text="")  #清除提示訊息
    yt=YouTube(url=input_url.get())
    if(input_url.get()==""):  #若未輸入網址就顯示提示訊息
        labelMsg.config(text="網址欄位必須輸入！")
    else:
        try:  #捕捉影片不存在的錯誤
            yt.url = input_url.get()  #取得輸入網址
            rbvalue = 1  #設定選項按鈕的值
            filename.set(yt.title)  #取得影片名稱
            for v1 in yt.streams:#建立影片格式串列
                # print(v1)
                listvideo.append(v1)
            for v2 in listvideo:  #建立影片格式選項按鈕
                rbtem = tk.Radiobutton(frame3, text=v2, variable=video, value=rbvalue, command=rbVideo)
                if(rbvalue==1):  #選取第1個選項按鈕       
                    rbtem.select()
                listradio.append(rbtem)  #建立選項按鈕串列        
                rbtem.grid(row=rbvalue-1, column=0, sticky="w")
                rbvalue += 1
            btnDown.config(state="normal")  #設定「下載影片」按鈕有效
        except:  #顯示影片不存在訊息
            labelMsg.config(text="找不到此 Youtube 影片！")
        
def rbVideo():  #點選選項按鈕後處理函式
    global strftype,itag
    labelMsg.config(text="")
    strvideo = str(listvideo[video.get()-1])  #取得點選項目
    print(strvideo)
    #取得影片型態
    start1 = strvideo.find("mime_type=")
    # print("START=",start1)
    end1 = strvideo.find("res")
    # print("ED=",end1)
    strftype = "."+strvideo[start1+17 : end1-2]
    print(strftype)
    #取得影片解析度
    end2 = strvideo.find("fps")
    strresolution = strvideo[end1+5 : end2-2]
    
    ID_start=strvideo.find("itag")
    ID_end=strvideo.find("mime")
    itag = strvideo[ID_start+6 : ID_end-2]#取得影片格式
        
def clickDown():  #按「下載影片」鈕後處理函式
    global itag, strftype, listradio
    labelMsg.config(text="")
    fpath = path.get()  #取得輸入存檔資料夾
    Streams=yt.streams.get_by_itag(itag)
    Streams.download(output_path=(fpath))
    for r in listradio:  #移除選項按鈕
        r.destroy()
    listradio.clear()  #清除串列
    listvideo.clear()
    input_url.set("")  #清除輸入框
    filename.set("")
    btnDown.config(state="disabled")  #設定「下載影片」按鈕無效

import tkinter as tk    
from pytube import YouTube

window=tk.Tk()
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


frame1=tk.Frame(window,width=450)
frame1.pack()
label1=tk.Label(frame1,text="Youtube網址：")
label1.pack()
entryUrl=tk.Entry(frame1,textvariable=input_url)
entryUrl.config(width=40)
btnUrl=tk.Button(frame1,text="確定",command=clickUrl)
label1.grid(row=0,column=0,sticky="e")  #sticky="e"文字靠右對齊
entryUrl.grid(row=0,column=1)
btnUrl.grid(row=0,column=2)

label2=tk.Label(frame1,text="存檔路徑")
entryPath = tk.Entry(frame1,textvariable=path)
entryPath.config(width=40)
label2.grid(row=1,column=0,pady=6,sticky="e")
entryPath.grid(row=1,column=1)

label3=tk.Label(frame1,text="檔案名稱")
entryFile=tk.Entry(frame1,textvariable=filename)
entryFile.config(width=40)
label3.grid(row=2,column=0,pady=3,sticky="e")
entryFile.grid(row=2,column=1)

frame2=tk.Frame(window)
frame2.pack()
btnDown=tk.Button(frame2,text="下載影片",command=clickDown)
btnDown.pack(pady=6)
btnDown.config(state="disabled")

labelMsg=tk.Label(window,text="",fg="red")  #提示訊息初始為空
labelMsg.pack()

frame3=tk.Frame(window)
frame3.pack()

window.mainloop()