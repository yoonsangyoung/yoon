from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait #엘리먼트 나올때까지 혹은 최대 지정시간까지 기다림 
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to keep browser open
options.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=service, options=options)
 
url = "https://hotels.naver.com/"
driver.get(url)

search2 = driver.find_element(By.CSS_SELECTOR,"input[title='한 달간 안보기']").click()
start = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[2]/div/div/div/div[1]/button").click().send_keys("서울")
# end = driver.find_element(By.CSS_SELECTOR,"input[id='destinationInput-input']").send_keys("오사카")

