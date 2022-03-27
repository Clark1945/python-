import os,shutil
cur_path=os.path.dirname(__file__)
tree_sample=os.walk(cur_path+"\\media")
outputdir='space2'

for dirname,subdir,files in tree_sample:#讀取資料夾名稱,下一層資料夾與資料夾中所有檔案   
    allfiles=[]
    basename=os.path.basename(dirname)
    if basename==outputdir:  #output區不重覆讀取
        continue
    for file in files:
        ext=file.split(".")[-1]
        if (ext == 'jpg' or ext == 'png'):  #圖片檔加入
            allfiles.append(file)
    
    if len(allfiles)>0:
        targetdir='media\\'+outputdir
        if not os.path.exists(targetdir):
            os.mkdir(targetdir)
        if(os.getcwd() != cur_path+"\\media\\space2"):
            os.chdir("./media/space2")
        counter=0
        for file in allfiles:
            filename=file.split(".")[0]
            m_filename="Cool Graphic"+str(counter)
            destfile=m_filename+"."+file.split(".")[1]
            srcfile=dirname+"\\"+file
            shutil.copy(srcfile,destfile)  
            counter+=1
        os.chdir("..")  #目錄還原
        os.chdir("..")  #目錄還原
print("更動完成")           
         