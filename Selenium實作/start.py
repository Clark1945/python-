from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
 
user_account=input("請輸入你的帳號\n")
user_pass=input("\n請輸入你的密碼\n")

options = Options()
options.add_argument("--disable-notifications")
#取消網頁的彈出視窗


chrome = webdriver.Chrome('./chromedriver', chrome_options=options)#建立webdriver物件，傳入瀏覽器驅動物件及瀏覽器設定。
chrome.get("https://www.facebook.com/")

email=chrome.find_element_by_id("email")
pw=chrome.find_element_by_id("pass")
#找出帳號密碼欄位

email.send_keys(user_account)
pw.send_keys(user_pass)
#填入帳號與密碼欄位

pw.submit()
#送出登入

time.sleep(3)
chrome.get('https://www.facebook.com/learncodewithmike')

for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
#執行滾動捲軸3次，一次停擺5秒

soup = BeautifulSoup(chrome.page_source, 'html.parser')
titles = soup.find_all('span', {
    'class': 'a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ojkyduve'})

for title in titles:
    post = title.find('span', {'dir': 'auto'})
    if post:
        print(post.getText())
#印出Text
chrome.quit()
#關閉
