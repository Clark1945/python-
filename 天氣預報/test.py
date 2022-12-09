import pandas as pd
import requests
from bs4 import BeautifulSoup
# df=pd.read_excel("712693030RPKUP4RX.xlsx",header=3) #從第四列開始
# df=df[["縣市名稱","區里代碼","區鄉鎮名稱"]]
# df.to_excel('district.xlsx',encoding='utf-8',index=False)

# url='https://www.cwb.gov.tw/V8/C/W/Town/MOD/3hr/1000401_3hr_PC.html?T=2022120917-1'
# # df=pd.read_html(url)[0]
# geturl=requests.get(url)
# if geturl.status_code != 200:
#     print("未成功訪問")
# soup=BeautifulSoup(geturl.text,'html.parser')
# all_data = soup.find_all("tr")
# for x in range(len(all_data)):
#     all_data