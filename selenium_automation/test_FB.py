from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
 
 
options = Options()
options.add_argument("--disable-notifications") #取消彈出視窗
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.facebook.com/") #開啟網頁

email=chrome.find_element_by_id("email")
pwd=chrome.find_element_by_id("pass")
#抓取帳密Element

email.send_keys("XX@gmail.com")
pwd.send_keys("XXX")
pwd.submit()
# 送出帳密並登入

time.sleep(5)
chrome.get('https://www.facebook.com/d.art.taipei')
time.sleep(5)

# # time.sleep(5)
# chat = chrome.find_element_by_css_selector(
#     '.xvijh9v')
# chat.click()
# # 如果有彈跳視窗，可以關閉 假如找不到可以用IDE挖出來www~

for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
#觸發滾輪事件

soup = BeautifulSoup(chrome.page_source, 'html.parser')
titles = soup.find_all('span', {
    'class': 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h'})
print(titles)