

import time

def todigit(n):
    if n<10:
        return '0'+str(n)
    else:
        retstr=str(n)
        return retstr

def convertDate(date):
    date_str=str(date)
    year_str=date_str[:3]
    realYear=str(int(year_str)+1911)
    realDate=realYear+date_str[4:6]+date_str[7:9]
    return realDate

import requests,re,time
import json,csv
import pandas as pd
import os
import matplotlib.pyplot as plt
from plotly.graph_objs import Scatter,Layout
from plotly.offline import plot


plt.rcParams["font.sans-serif"]="mingliu" #中文字型
plt.rcParams["axes.unicode_minus"]=False

pd.options.mode.chained_assignment=None

url_base = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2021'
url_tail='01&stockNo=2330&_=1670560076969'
file_path='stock_year.csv'

if not os.path.isfile(file_path):
    for i in range(1,13):
        url_twse=url_base+todigit(i)+url_tail
    # url_twse='https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210801&stockNo=2330&_=1670560076969'
        res=requests.get(url_twse)
        json_data=json.loads(res.text)
        outputFile=open(file_path,'a',newline='',encoding='UTF-8')
        outputWriter=csv.writer(outputFile)
        if i==1:
            outputWriter.writerow(json_data['fields'])
        
        for dataLine in (json_data['data']):
            outputWriter.writerow(dataLine)
        time.sleep(0.5)
    outputFile.close()

pdstock=pd.read_csv(file_path,encoding='UTF-8')
for i in range(len(pdstock['日期'])):
    pdstock['日期'][i] = convertDate(pdstock['日期'][i])
pdstock['日期']=pd.to_datetime(pdstock['日期'])

data=[
    Scatter(x=pdstock['日期'],y=pdstock['收盤價'],name='收盤價'),
    Scatter(x=pdstock['日期'],y=pdstock['最低價'],name='最低價'),
    Scatter(x=pdstock['日期'],y=pdstock['最高價'],name='最高價')
]
plot({"data":data,"layout": Layout(title='2019年年度個股統計')},auto_open=False)

pcode=re.search('stockNo=(\d+)',url_tail).group(1)
df_plot=pdstock.plot(kind='line',figsize=(12,6),x="日期",y=["收盤價","最低價","最高價"],title=pcode+'_'+file_path) #畫統計圖