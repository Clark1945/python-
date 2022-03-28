import os,hashlib
curpath=os.path.dirname(__file__)
sampletree=os.walk(curpath+"\media\check_pic_space1")
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
            allfile.append(dirname+"\\"+file) 
            
        if len(allfile)>0:
            for imagefile in allfile:
                img_md5=hashlib.md5(open(imagefile,'rb').read()).digest() #
                if not img_md5 in allmd5s:
                    allmd5s[img_md5]=str(imagefile)
                    
    for samefile in allfile:
        if not samefile in allmd5s.values():
            samedict.append(samefile)
    samenum=len(allfile)-len(allmd5s)
sameset=set(samedict)
print("在{}張照片中共有{}張重複，重複的有:".format(len(allfile),samenum)) 
for evfile in sameset:
    print(evfile,sep="\n")
print("完成")