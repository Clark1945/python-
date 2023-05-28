import os,hashlib

curpath=os.path.dirname(__file__)
sampletree=os.walk(curpath+"\media\check_pic_space1")#檢查區域

n=0
allmd5s=dict()
samenum=0
samedict=[]
sameset=set()

for dirname,subdir,files in sampletree:
    allfile=[]
    for file in files:
        ext=file.split('.')[-1]
        if (ext=="png" or ext=="jpg"): 
            allfile.append(dirname+"\\"+file)  #所有的圖片檔
            
    if len(allfile)>0:
        for imagefile in allfile:
            img_md5=hashlib.md5(open(imagefile,'rb').read()).digest() #
            if not img_md5 in allmd5s:
                allmd5s[img_md5]=str(imagefile) #非重複的圖片
                    
    for samefile in allfile:
        if not samefile in allmd5s.values():
            samedict.append(samefile) #重複的圖片檔名與路徑
    samenum=len(allfile)-len(allmd5s) #重複的圖片數量
sameset=set(samedict)
print("在{}張照片中共有{}張重複，重複的有:".format(len(allfile),samenum)) 
for evfile in sameset:
    print(evfile,sep="\n") #印出所有重複的圖片路徑

print("完成")