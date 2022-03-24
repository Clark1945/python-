import cv2,subprocess
img=cv2.imread('media\\bank.jpg')
cv2.namedWindow("Image")
cv2.imshow("Image",img)  #顯示圖片
cv2.waitKey(0)
cv2.destroyWindow("Image")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #轉為灰階圖片
_, inv=cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) #轉為黑白  _用來去除雜值

for i in range(len(inv)):
    for j in range(len(inv[i])):
        if inv[i][j] ==255:
            count=0
            for k in range(-4,3):#設定範圍檢查，判斷是否雜點
                for l in range(-4,3):
                    try:
                        if inv[i+k][j+1]==255:
                            count+=1
                    except IndexError:
                        pass
            if count <=7: #周圍小於七個白點則將白點去除
                inv[i][j]=0                
dilation=cv2.dilate(inv,(8,8),iterations=1)  #圖形加粗
cv2.imwrite("media\\bank_result.jpg",dilation)  #存檔

child = subprocess.Popen('tesseract media\\bank_result.jpg media\\result')  #OCR辨識
child.wait()
text = open('media\\result.txt').read().strip()
print("驗證碼為 " + text)
                    
            