def rbCity():  #點選縣市選項按鈕後處理函式
    global sitelist, listradio
    sitelist.clear()  #清除原有測站串列
    for r in listradio:  #移除原有測站選項按鈕
        r.destroy()
    for c1 in citylist:  
        if(c1 ==  city.get()):#是第1個縣市的測站
            sitelist.append(df[(df.縣市==c1)])
    print(sitelist)        
    # sitemake()  #建立測站選項按鈕
    # rbSite()  #顯示PM2.5訊息
    print()
    
def rbSite():  #點選測站選項按鈕後處理函式
    n = 0
    for s in df[(df.縣市==c1)]:  #逐一取得測站 
            if (s.站點 == site.get()):
                pm = s.PM2_5  #取得PM2.5的值
                print(pm)
                if(pd.isnull(pm)):  #如果沒有資料
                    result1.set(s + "站的 PM2.5 值目前無資料！")
                else:  #如果有資料
                    if(pm <= 35):  #轉換為等級
                        grade1 = "低"
                    elif(pm <= 53):
                        grade1 = "中"
                    elif(pm <= 70):
                        grade1 = "高"
                    else:
                        grade1 = "非常高"
                    result1.set(s + "站的 PM2.5 值為「" + str(pm) + "」：「" + grade1 + "」等級")
            break  #找到點選測站就離開迴圈
    n += 1
    print()
    
def clickRefresh():  #重新讀取資料
    # global data
    # data = pd.read_csv("http://opendata.epa.gov.tw/ws/Data/REWXQA/?$orderby=SiteName&$skip=0&$top=1000&format=csv")
    # rbSite()  #更新測站資料
    print()
    
def sitemake():  #建立測站選項按鈕
    # global sitelist, listradio
    # print(sitelist)
    # for c1 in sitelist:  #逐一建立選項按鈕
        # rbtem = tk.Radiobutton(frame2, text=c1, variable=site, value=c1)  #建立選項按鈕# command=rbSite
        # listradio.append(rbtem)  #加入選項按鈕串列
        # if(c1==sitelist[0]):  #預設選取第1個項目         
        #     rbtem.select()
        # rbtem.pack(side="left")  #靠左排列 
        print()

        
import tkinter as tk
import pandas as pd
import requests
api_url="https://data.epa.gov.tw/api/v2/aqx_p_02?limit=1000&api_key=eaf2fb82-209a-4a4d-af1e-7a053cf034db"
response=requests.get(api_url)
api=response.json()['records']
data2=[]
for dic in api :
    dic.pop("itemunit")
    data2.append(dic)
data3=[]
# print(data2)
for x in data2:
        data3.append([x['county'],x['site'],x['pm25'],x['datacreationdate']])
columns=["縣市","站點","PM25","探測日期"]
df=pd.DataFrame(data3,columns=columns)
# print(data3)
print(df.PM2_5)

win=tk.Tk()
win.geometry("640x270")
win.title("PM2.5 實時監測")

city = tk.StringVar()  #縣市文字變數
site = tk.StringVar()  #測站文字變數
result1 = tk.StringVar()  #訊息文字變數
citylist = []  #縣市串列
sitelist = []  #鄉鎮串列
listradio = []  #鄉鎮選項按鈕串列
# print(df["縣市"])
#建立縣市串列
for c1 in df['縣市']:  
    if(c1 not in citylist):  #如果串列中無該縣市就將其加入
        citylist.append(c1)
#建立第1個縣市的測站串列
count = 0
for c1 in citylist:  
    if(c1 ==  citylist[0]):#是第1個縣市的測站
        sitelist.append(df[(df.縣市==c1)])
label1 = tk.Label(win, text="縣市：", pady=6, fg="blue", font=("新細明體", 12))
label1.pack()
frame1 = tk.Frame(win)  #縣市容器
frame1.pack()
for i in range(0,3):  #3列選項按鈕
    for j in range(0,8):  #每列8個選項按鈕
        n = i * 8 + j  #第n個選項按鈕
        if(n < len(citylist)):
            city1 = citylist[n]  #取得縣市名稱
            rbtem = tk.Radiobutton(frame1, text=city1, variable=city, value=city1, command=rbCity)  #建立選項按鈕
            rbtem.grid(row=i, column=j)  #設定選項按鈕位置
            if(n==0):  #選取第1個縣市
                rbtem.select()

label2 = tk.Label(win, text="測站：", pady=6, fg="blue", font=("新細明體", 12))
label2.pack()
frame2 = tk.Frame(win)  #測站容器
frame2.pack()
# sitemake()

btnDown = tk.Button(win, text="更新資料", font=("新細明體", 12), command=clickRefresh)
btnDown.pack(pady=6)
lblResult1 = tk.Label(win, textvariable=result1, fg="red", font=("新細明體", 16))
lblResult1.pack(pady=6)
# rbSite()  #顯示測站訊息

win.mainloop()