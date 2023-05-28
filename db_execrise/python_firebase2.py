def menu():
    os.system("cls")
    print("英文單字")
    print("----------------------------------")
    print("1.查詢單字")
    print("2.新增單字")
    print("3.顯示單字")
    print("4.修改單字")
    print("5.刪除單字")
    print("0.結束運作")
    print("----------------------------------")
    
def input_data():
    global datas
    while True:
        eword=input("請輸入英文單字(Enter==>停止輸入)")
        if eword=="":break
        keyid=CheckKey(eword)  #取得DB中的英文單字
        if keyid!="":
            print("{}單字已存在!".format(datas[keyid]))
            continue
        cword=input("請輸入中文翻譯:")
        word={"eword":eword,"cword":cword}
        keyid=fb.post(url,word)["name"]
        time.sleep(2)
        if datas==None:datas=dict()
        datas[keyid]=word
        print("{}以儲存完畢".format(word))
        
def disp_data():
    global datas
    datas=fb.get(url,None)
    if datas!=None:
        n,page=0,15
        for key in datas:
            if n%page==0:
                print("單字\t中文翻譯")
                print("-----------------------")
            print("{}\t{}".format(datas[key]["eword"],datas[key]["cword"]))
            n+=1
            if n==page:
                c=input("請按Enter顯示下一頁，Q返回主選單")
                if c.upper()=="Q":return
                n=0
            c=input("按下任意鍵返回主選單")
            
def search_data():
    while True:
        eword=input("請輸入要查詢的英文單字(Enter==>停止輸入)")
        if eword =="":break
        keyid=CheckKey(eword)
        if keyid !="":
            print("中文翻譯:{}".format(datas[keyid]["cword"]))
        else:
            print("{}未建立".format(eword))
        input("按下任意鍵繼續查詢")
        
def edit_data():
    while True:
        eword=input("請輸入要修改的英文單字(Enter==>停止輸入)")
        if eword=="": break
        keyid=CheckKey(eword)
        if keyid!="":
            print("原來中文翻譯:{}".format(datas[keyid]["cword"]))
            cword=input("請輸入中文翻譯")
            word={"eword":eword,"cword":cword}
            datas[keyid]=word  #加入List
            fb.put(url+"/",data=word,name=keyid) #加入資料DB
            time.sleep(2)
            print("{}已修改完畢\n".format(word))
        else:
            print("{}未建立\n".format(eword))

def delete_data():
    while True:
        eword=input("請輸入要刪除的英文單字(Enter停止輸入)")
        if eword=="":break
        keyid=CheckKey(eword)
        if keyid!="":
            print("確定刪除{}的資料".format(datas.get(keyid)))
            yn=input("(Y/N)?")
            if (yn.upper()=="Y"):
                fb.delete(url+"/"+keyid,None)
                datas.pop(keyid)
                print("資料刪除完畢\n")
        else:
            print("{}資料未建立".format(eword))
                
def CheckKey(en):
    keyid=""
    if datas!=None:
        for key in datas:
            if en==datas[key]["eword"]:
                keyid=key
                break
    return keyid

import os,time
from firebase import firebase 

url="https://pythontry01-default-rtdb.firebaseio.com/English"
fb=firebase.FirebaseApplication(url,None)
datas=fb.get(url,None)

# with open("media/word.csv",encoding="UTF-8-sig")as f:
#     for line in f:
#         eword,cword=line.rstrip("\n").split(",")
#         word={"eword":eword,"cword":cword}
#         if CheckKey(eword)== "":
#             # fb.post(url,word)
#             print(word)

while True:
    menu()
    choice=input("請輸入你要使用的功能")
    try:
        choice=int(choice)
        if choice==1:
            search_data()
        elif choice==2:
            input_data()
        elif choice==3:
            disp_data()
        elif choice==4:
            edit_data()
        elif choice==5:
            delete_data()
        else:
            break
    except:
        print("無此功能")
        time.sleep(2)
        
print("執行完畢")