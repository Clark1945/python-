import os
from PIL import Image

output_dir='setsize_space2'#Output區域
input_dir='setsize_space'#Input區域
image_width=800#要轉換的寬度
image_height=600#要轉換的高度

cur_path=os.path.dirname(__file__)
sampletree=os.walk(cur_path)

for dirname,subdir,allfiles in sampletree:
    allfile=[]
    basename=os.path.basename(dirname)
    if basename==input_dir:
        for file in allfiles:
            ext=file.split(".")[-1]
            if ext=="png" or ext=="jpg":
                allfile.append(dirname+"/"+file)
        if len(allfile)>0:
            target_dir=dirname+"/"+output_dir
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
            for file in allfile:
                pathname,filename=os.path.split(file)
                img=Image.open(file)
                w,h=img.size
                img=img.resize((image_width,image_height))
                img.save(target_dir+"/"+filename)
                print("<{}> 複製完成".format(target_dir+"/"+filename))
                img.close()
print("完成")                
