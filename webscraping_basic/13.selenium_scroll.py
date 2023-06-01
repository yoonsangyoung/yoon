from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #엘리먼트 나올때까지 혹은 최대 지정시간까지 기다림 
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

##
import time
 
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to keep browser open
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.google.com/search?q=%ED%95%B4%EB%A6%B0&sxsrf=APwXEdeWCIrUYdWjKRjXaYUx04jUptUsKQ:1681869719722&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjB9M757LT-AhXEr1YBHbR3BPQQ_AUoAXoECAEQAw&biw=1196&bih=1072&dpr=1.5"
driver.get(url)
#스크롤 끝 까지 내리기
prev_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#최대 밑으로
    time.sleep(2)
    curr_height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(2)
    if curr_height == prev_height:
        break
    prev_height = curr_height
print("finish")

##
from bs4 import BeautifulSoup
import requests

headers ={"User-Agent":"ozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status
soup = BeautifulSoup(driver.page_source,'html.parser') 
    
# imgs = soup.find_all("span",attrs={"class":"OztcRd goedYd cS4Vcb-pGL6qe-mji9Ze"})
# for img in imgs:
#     print(img.get_text())


# url = "https://www.google.com/search?q=%ED%95%B4%EB%A6%B0&sxsrf=APwXEdeWCIrUYdWjKRjXaYUx04jUptUsKQ:1681869719722&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjB9M757LT-AhXEr1YBHbR3BPQQ_AUoAXoECAEQAw&biw=1196&bih=1072&dpr=1.5"
# headers ={"User-Agent":"ozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
# res=requests.get(url,headers=headers)
# res.raise_for_status
# soup = BeautifulSoup(res.text, 'html.parser') 
    
# imgs = soup.find_all("a",attrs={"class":"Si6A0c itIJzb"})
# for idx, img_div in enumerate(imgs):
#     img = img_div.find("img")
#     img_data = requests.get(img["src"]).content
#     with open("img{}.jpg".format(idx+1), "wb") as f:
#                 f.write(img_data)
    