import requests
from bs4 import BeautifulSoup
import datetime

def udn_global():
    ori_url="https://udn.com"
    response=requests.get("https://udn.com/news/cate/2/7225")
    soup=BeautifulSoup(response.text,"html.parser")
    print("聯合新聞網──全球")
    print("日期",datetime.date.today())
    column=soup.find_all("div",class_="story-list__text")
    for title in column:
        try:
            title2=title.h2.a.text
            print(title2)
            the_url=title.h2.a.get("href")
            print(ori_url+the_url)
        except:
            pass
        
def udn_local():
    ori_url="https://udn.com"
    response=requests.get("https://udn.com/news/cate/2/6641")
    soup=BeautifulSoup(response.text,"html.parser")
    print("聯合新聞網──地方")
    print("日期",datetime.date.today())
    column=soup.find_all("div",class_="story-list__text")
    for title in column:
        try:
            title2=title.h2.a.text
            print(title2)
            the_url=title.h2.a.get("href")
            print(ori_url+the_url)
        except:
            pass
        
def udn_industrial_economics():
    ori_url="https://udn.com"
    response=requests.get("https://udn.com/news/cate/2/6644")
    soup=BeautifulSoup(response.text,"html.parser")
    print("聯合新聞網──產業經濟新聞")
    print("日期",datetime.date.today())
    column=soup.find_all("div",class_="story-list__text")
    for title in column:
        try:
            title2=title.h2.a.text
            print(title2)
            the_url=title.h2.a.get("href")
            print(ori_url+the_url)
        except:
            pass
        
def udn_stocks_market():
    ori_url="https://udn.com"
    response=requests.get("https://udn.com/news/cate/2/6645")
    soup=BeautifulSoup(response.text,"html.parser")
    print("聯合新聞網──股市新聞")
    print("日期",datetime.date.today())
    column=soup.find_all("div",class_="story-list__text")
    for title in column:
        try:
            title2=title.h2.a.text
            print(title2)
            the_url=title.h2.a.get("href")
            print(ori_url+the_url)
        except:
            pass
        
def udn_travel():
    ori_url="https://udn.com"
    response=requests.get("https://udn.com/news/cate/1013")
    soup=BeautifulSoup(response.text,"html.parser")
    print("聯合新聞網──旅遊版")
    print("日期",datetime.date.today())
    column=soup.find_all("div",class_="story-list__text")
    for title in column:
        try:
            title2=title.h2.a.text
            print(title2)
            the_url=title.h2.a.get("href")
            print(ori_url+the_url)
        except:
            pass
# udn_global()
# udn_local()
# udn_industrial_economics()
# udn_stocks_market()
# udn_travel()
