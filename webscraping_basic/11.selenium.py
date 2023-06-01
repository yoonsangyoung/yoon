from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #엘리먼트 나올때까지 혹은 최대 지정시간까지 기다림 
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to keep browser open
driver = webdriver.Chrome(service=service, options=options)

driver.get(url="https://www.naver.com")

# login_link1 = driver.find_element(By.CLASS_NAME,'link_login').click()
# id = driver.find_element(By.NAME, "id").send_keys("dbsqa")
# pw = driver.find_element(By.NAME, "pw").send_keys("DBStkddud1!")
# login = driver.find_element(By.CLASS_NAME, "btn_login").click()

time.sleep(1)
search1 = driver.find_element(By.CSS_SELECTOR,"input[name='query']").send_keys("본동 신동아")
search2 = driver.find_element(By.XPATH, "//*[@id='search_btn']").click()

search3 = driver.find_element(By.XPATH, "//*[@id='main_pack']/section[1]/div[1]/div[2]/div[2]/div[5]/div[3]/div[2]/ul/li[4]/span[2]/a").click()

element = driver.find_element(By.CLASS_NAME, "address_filter")
checkbox = element.find_element(By.CSS_SELECTOR, "input[class='checkbox_label']")
checkbox.click()