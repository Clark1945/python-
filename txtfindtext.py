import os
curpath=os.path.dirname(__file__)
sampletree=os.walk(curpath)
keyword=input("請輸入想要查找的單詞")

for dirname,subdir,allfiles in sampletree:
    allfile=[]
    for file in allfiles:
        ext=file.split(".")[-1]
        if ext=="py"or ext=="txt":
            allfile.append(dirname+"/"+file)
        
    if len(allfile)>0:
        for file in allfile:
            try:
                fp=open(file,"r",encoding="UTF-8")
                article=fp.readlines()
                fp.close()
                line=0
                for row in article:
                    line+=1
                    if keyword in row:
                        print("在{}，第{}列找到「{}」".format(file,line,keyword))
            except:
                print("{}無法讀取...".format(file))
print("完成")