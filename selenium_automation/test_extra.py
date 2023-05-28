from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

def selenium_chrome_demo(input_url, input_action_list, headless_mode=False):
    # 0. init
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    # 1. set headless
    if headless_mode:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
    # 2. set user-agent (假造User-Agent 作為Header)
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) " \
         "AppleWebKit/537.36 (KHTML, like Gecko) " \
         "Chrome/92.0.4515.159 Safari/537.36"
    chrome_options.add_argument('user-agent={}'.format(ua))
    # 3. open browser
    driver = webdriver.Chrome("./chromedriver",
                              options=chrome_options)
    driver.set_window_size(1024, 768)
    # 4. run action
    
    try:
        driver.implicitly_wait(10)
        driver.get(input_url)
        for temp_action in input_action_list:
            if temp_action['type'] == 'click':
                driver.find_element(By.XPATH, temp_action['xpath']).click()
            if temp_action['type'] == 'write':
                driver.find_element(By.XPATH, temp_action['xpath']).send_keys(temp_action['text'])
    except Exception as ex:
        print('Exception:' + str(ex))
    finally:
        driver.quit()
    return

test_json_list = [
{'type': 'write', 'xpath': '//*[@id="account"]', 'text': 'account'},
{'type': 'write', 'xpath': '//*[@id="password"]', 'text': 'password'},
{'type': 'click', 'xpath': '/html/body/div/div/div/form/button', 'text': ''}]

selenium_chrome_demo(input_url="https://member.ithome.com.tw/login",
                     input_action_list=test_json_list)