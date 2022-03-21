import pandas as pd
import requests
api_url="https://data.epa.gov.tw/api/v2/aqx_p_02?limit=1000&api_key=eaf2fb82-209a-4a4d-af1e-7a053cf034db"
response=requests.get(api_url)
api=response.json()['records']
# print(response.status_code)
data2=[]

for dic in api :
    dic.pop("itemunit")
    data2.append(dic)
data3=[]
for x in data2:
        data3.append([x['county'],x['site'],x['pm25'],x['datacreationdate']])
columns=["縣市","站點","PM2.5","探測日期"]
df=pd.DataFrame(data3,columns=columns)
print(df)