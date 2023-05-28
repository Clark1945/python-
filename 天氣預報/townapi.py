from flask import Flask,render_template
app = Flask(__name__) #建立app物件
import plotly as py
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import json

@app.route('/')
def noPage():
    return 'Please type the area to get more information.'

@app.route('/<town>') # 網址加入參數
def index(town):
    if not os.path.isfile('district.xlsx'):
        df=pd.read_excel("712693030RPKUP4RX.xlsx",header=3) #從第四列開始
        df=df[["縣市名稱","區里代碼","區鄉鎮名稱"]]
        df=df.drop_duplicates()
        df.to_excel('district.xlsx',encoding='utf-8',index=False)

    df_town=pd.read_excel('district.xlsx')
    dfs=df_town[(df_town["縣市名稱"]==town[0:3])&(df_town["區鄉鎮名稱"]==town[3:])]

    if len(dfs)>0:
        town_no=str(dfs.iloc[0,1])# 區里代碼
        url='https://www.cwb.gov.tw/V8/C/W/Town/MOD/3hr/'+town_no+'_3hr_PC.html?T=2022120917-1'
        geturl=requests.get(url)
        if geturl.status_code != 200:
            print("未成功訪問")
        soup=BeautifulSoup(geturl.text,'html.parser')
        all_data = soup.find_all("tr")

        measurement_columns=[]
        measurement_date=[]
        measurement_time=[]
        measurement_weather=[]
        measurement_temperature=[]
        measurement_bodyTemperature=[]
        measurement_rain=[]
        measurement_wet=[]
        measurement_wind=[]
        measurement_windS=[]
        measurement_windDirection=[]
        measurement_comfort=[]

        for x in range(len(all_data)):
            measurement_columns.append(all_data[x].th.text)
            if all_data[x].th.text=="日期":
                for y in range(1,len(all_data[x].find_all('th'))):
                    measurement_date.append(all_data[x].find_all('th')[y].text)
            if all_data[x].th.text=="時間":
                for y in range(1,len(all_data[x].find_all('th'))):
                    measurement_time.append(all_data[x].find_all('th')[y].text)
            if all_data[x].th.text=="天氣狀況":
                for y in range(len(all_data[x].find_all('td'))):
                    measurement_weather.append(all_data[x].find_all('td')[y].img.get("title"))
            if all_data[x].th.text=="溫度":
                for y in range(len(all_data[x].find_all('td'))):
                    temperature = all_data[x].find_all('td')[y].text[0:2]
                    measurement_temperature.append(temperature)
            if all_data[x].th.text=="體感溫度":
                for y in range(len(all_data[x].find_all('td'))):
                    measurement_bodyTemperature.append(all_data[x].find_all('td')[y].text[0:2])
            if all_data[x].th.text=="降雨機率":
                for y in range(len(all_data[x].find_all('td'))):
                    measurement_rain.append(all_data[x].find_all('td')[y].text)
            if all_data[x].th.text=="相對濕度":
                for y in range(len(all_data[x].find_all('td'))):
                    measurement_wet.append(all_data[x].find_all('td')[y].text)
            if all_data[x].th.text=="蒲福風級":
                for y in range(len(all_data[x].find_all('td'))):
                    measurement_wind.append(all_data[x].find_all('td')[y].text)
            if all_data[x].th.text=="風速(m/s)":
                for y in range(len(all_data[x].find_all('td'))):
                    measurement_windS.append(all_data[x].find_all('td')[y].text)
            if all_data[x].th.text=="風向":
                for y in range(len(all_data[x].find_all('td'))):
                    measurement_windDirection.append(all_data[x].find_all('td')[y].text)
            if all_data[x].th.text=="舒適度":
                for y in range(len(all_data[x].find_all('td'))):
                    measurement_comfort.append(all_data[x].find_all('td')[y].text) 

                    
        df=pd.DataFrame(columns=measurement_columns)

        temp_date=[]
        cnt=0
        for x in range(len(measurement_time)):
            if measurement_time[x] != "00:00":
                temp_date.append(measurement_date[cnt])
            else:
                cnt+=1
                temp_date.append(measurement_date[cnt])      
        

        measurement_rain2=[]
        for x in range(len(measurement_rain)):
            measurement_rain2.append(measurement_rain[x])
            measurement_rain2.append(measurement_rain[x])
        measurement_rain2=measurement_rain2[:len(measurement_rain2)-1]
        

        df["日期"]=temp_date
        df["時間"]=measurement_time
        df["天氣狀況"]=measurement_weather
        df["溫度"]=measurement_temperature
        df["體感溫度"]=measurement_bodyTemperature
        df["降雨機率"]=measurement_rain2
        df["相對濕度"]=measurement_wet
        df["蒲福風級"]=measurement_wind
        df["風速(m/s)"]=measurement_windS
        df["風向"]=measurement_windDirection
        df["舒適度"]=measurement_comfort

        values = [temp_date,measurement_time,measurement_weather,measurement_temperature,measurement_bodyTemperature,measurement_rain2,measurement_wet,measurement_wind,measurement_windS,\
            measurement_windDirection,measurement_comfort
]       
        table = {
        'type': 'table',
        'header': {
            'values': [["<b>日期</b>"], ["<b>時間</b>"],
                        ["<b>天氣狀況</b>"], ["<b>溫度</b>"], ["<b>體感溫度</b>"],["<b>降雨機率</b>"],["<b>相對濕度</b>"],["<b>蒲福風級</b>"],["<b>風速</b>"],["<b>風向</b>"],["<b>舒適度</b>"]],
            'align': "center",
            'line': {'width': 1, 'color': 'black'},
            'fill': {'color': "grey"},
            'font': {'family': "Arial", 'size': 24, 'color': "white"},
            'height': 35
        },
        'cells': {
            'values': values,
            'align': "center",
            'line': {'color': "black", 'width': 1},
            'font': {'family': "Arial", 'size': 22, 'color': ["black"]},
            'height': 35
  }
}

        # 將相關圖表物件以list方式寫入
        graphs = [
            dict(
                data=
                    [table]
                ,
                layout=dict(
                    width=1920,
                    height=1080,
                )
            )
        ]
        # 序列化
        graphJSON = json.dumps(graphs, cls=py.utils.PlotlyJSONEncoder)

        return render_template('pyplot.html', graphJSON=graphJSON) # 回傳html的template
        return df.to_json(orient='records',force_ascii=False) #將所有資料用JSON格式回傳
    else:
        return "無此名稱"

if __name__=='__main__':
    app.run()