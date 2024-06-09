import time
from firebase import firebase
url='https://pythontry01-default-rtdb.firebaseio.com'
fb=firebase.FirebaseApplication(url,None)

students=[{"no":1,"name":"Den"},{"no":2,"name":"Dan"},{"no":3,"name":"Damn"}]
for student in students:
    fb.post("/stu",student)
    print("{}儲存完畢。".format(student))

def CheckKey(no):
    keyid=""
    if datas!=None:
        for key in datas:
            if no==datas[key]["no"]:
                keyid=key
                break
    return keyid

while True:
    datas=fb.get("/stu",None)
    no=input("請輸入座號:(Enter停止輸入)")
    if no=="":break
    keyid=CheckKey(int(no))
    if keyid !="" :
        print("確定刪除{}的資料".format(datas[keyid]["name"]))
        yn=input("(Y/N)?")
        if(yn=="Y" or yn=="y"):
            fb.delete("/stu/"+keyid,None)
            print("已刪除")
    else:
        print("{}未建立".format(no))
    