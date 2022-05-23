import os,shutil
cur_path=os.path.dirname(__file__)
tree_sample=os.walk(cur_path+"\\media")
outputdir='space2'#輸出資料夾
inputdir='space1'#輸入資料夾

for dirname,subdir,files in tree_sample:#讀取資料夾名稱,下一層資料夾與資料夾中所有檔案   
    allfiles=[]
    basename=os.path.basename(dirname)
    if basename==outputdir:  #output區不重覆讀取
        continue
    if basename==inputdir:
        for file in files:
            ext=file.split(".")[-1]
            if (ext == 'jpg' or ext == 'png'):  
                allfiles.append(file)#加入除了output區外的所有圖片檔
        if len(allfiles)>0:
            targetdir='media\\'+outputdir
            if not os.path.exists(targetdir):#檢查output區是否存在，無則新增一個
                os.mkdir(targetdir)
            if(os.getcwd() != cur_path+"\\media\\space2"):#如當前目錄不位於output區，則轉到output區
                os.chdir("./media/space2")
            counter=0
            for file in allfiles:
                filename=file.split(".")[0]
                m_filename="Cool Graphic"+str(counter)#儲存圖片使用的統一檔名
                destfile=m_filename+"."+file.split(".")[1]#檔名結合副檔名
                srcfile=dirname+"\\"+file
                shutil.copy(srcfile,destfile)  #複製與貼上
                counter+=1
            os.chdir("..")  #目錄還原
            os.chdir("..")  #目錄還原
print("更動完成")           
         