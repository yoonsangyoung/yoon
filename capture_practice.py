from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #엘리먼트 나올때까지 혹은 최대 지정시간까지 기다림 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

##
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.drawing.image import Image as XLImage

from openpyxl.drawing.image import Image
from PIL import Image as PILImage
from io import BytesIO

import urllib.request
import time


from collections import Counter
import re
import os

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to keep browser open
driver = webdriver.Chrome(service=service, options=options)

wb = load_workbook("Kream.xlsx")
ws1 = wb["원본데이터"]


model_list = [cell.value for cell in ws1["B"]]
dic_model_list = Counter(model_list)
serach_list = [k for k,v in dic_model_list.items() if v>=50]

print(serach_list,len(serach_list))

# ##

url = "https://kream.co.kr/login"
driver.get(url)
driver.maximize_window()

driver.find_element(By.XPATH,"//*[@id='wrap']/div[2]/div/div/div[1]/div/input").send_keys("dbsqa@naver.com")
driver.find_element(By.XPATH,"//*[@id='wrap']/div[2]/div/div/div[2]/div/input").send_keys("Xe0hJd#U")
login = driver.find_element(By.XPATH,'//*[@id="wrap"]/div[2]/div/div/div[3]/a').click()
time.sleep(2)

ws2 = wb["시세"]
cnt = 0

for data  in serach_list:
    cnt+=1
    url = "https://kream.co.kr/search?keyword="+data
    print(url,"//",cnt)
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"div.product").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"strong.title").click()
    time.sleep(2)
    price_records = driver.find_elements(By.CLASS_NAME,"select_item")
    
    
    Capture = driver.get_screenshot_as_png()
    Capture = PILImage.open(BytesIO(Capture))  
    crop = Capture.crop((1900, 250, 3250, 1600))
    image_path = os.path.join("static/images", data + ".png")
    crop.save(image_path)

    