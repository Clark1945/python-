import os,docx
curpath=os.path.dirname(__file__)
sampletree=os.walk(curpath)

keyword=input("輸入你要搜尋的字串：\n")
print("搜尋字串為:{}".format(keyword))
for dirname,subdir,allfiles in sampletree:
    allfile=[]
    for file in allfiles:
        ext=file.split(".")[-1]
        if ext=="docx":
            allfile.append(dirname+"/"+file)
    for file in allfile:
        print("正在搜尋<{}>...".format(file))
        try:
            doc=docx.Document(file)
            line=0
            for p in doc.paragraphs:
                line+=1
                if keyword in p.text:
                    print("...在第{}段文字中找到「{}」\n{}。".format(line,keyword,p.text))
        except:
            print("無法讀取{}檔案...".format(file))
            
print("讀取完畢")