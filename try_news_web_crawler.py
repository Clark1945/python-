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
                nowday=title.div.time.text[0:10]
                if nowday == str(datetime.date.today()):
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
                nowday=title.div.time.text[0:10]
                if nowday == str(datetime.date.today()):
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
                nowday=title.div.time.text[0:10]
                if nowday == str(datetime.date.today()):
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
                nowday=title.div.time.text[0:10]
                if nowday == str(datetime.date.today()):
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
                nowday=title.div.time.text[0:10]
                if nowday == str(datetime.date.today()):
                    title2=title.h2.a.text
                    print(title2)
                    the_url=title.h2.a.get("href")
                    print(ori_url+the_url)
            except:
                pass

def chi_money():
    ori_url="https://www.chinatimes.com"
    response=requests.get("https://www.chinatimes.com/world/total?chdtv")
    soup=BeautifulSoup(response.text,"html.parser")
    print("中國時報──財經")
    print("日期",datetime.date.today())
    column=soup.find_all("div",class_="col")
    for title in column:
        title3=title.find("div",class_="meta-info").time.get("datetime")
        today=title3[0:10]
        if today == str(datetime.date.today()):
            try:
                title2=title.a.text
                print(title2)
                the_url=title.a.get("href")
                print(ori_url+the_url)
            except:
                pass
            
def chi_world():
    ori_url="https://www.chinatimes.com"
    response=requests.get("https://www.chinatimes.com/world/total?chdtv")
    soup=BeautifulSoup(response.text,"html.parser")
    print("中國時報──國際")
    print("日期",datetime.date.today())
    column=soup.find_all("div",class_="col")
    for title in column:
        title3=title.find("div",class_="meta-info").time.get("datetime")
        today=title3[0:10]
        if today == str(datetime.date.today()):
            try:
                title2=title.a.text
                print(title2)
                the_url=title.a.get("href")
                print(ori_url+the_url)
            except:
                pass

def chi_tech():
    ori_url="https://www.chinatimes.com"
    response=requests.get("https://www.chinatimes.com/technologynews/total?page=1&chdtv")
    soup=BeautifulSoup(response.text,"html.parser")
    print("中國時報──科技")
    print("日期",datetime.date.today())
    column=soup.find_all("div",class_="col")
    for title in column:
        title3=title.find("div",class_="meta-info").time.get("datetime")
        today=title3[0:10]
        if today == str(datetime.date.today()):
            try:
                title2=title.a.text
                print(title2)
                the_url=title.a.get("href")
                print(ori_url+the_url)
            except:
                pass
            
def ltn_world():
    response=requests.get("https://news.ltn.com.tw/list/breakingnews/world")
    soup=BeautifulSoup(response.text,"html.parser")
    print("自由時報")
    print("日期",datetime.date.today())
    article=soup.find("div",class_="whitecon boxTitle").ul
    # print(article)
    x=article.find_all("li")
    for y in x:
        print(y.a.get("title"))
        print(y.a.get("href"))

# udn_global()
# udn_local()
# udn_industrial_economics()
# udn_stocks_market()
# udn_travel()
# chi_money()
# chi_world()
# chi_tech()
# chi_world()
# ltn_world()