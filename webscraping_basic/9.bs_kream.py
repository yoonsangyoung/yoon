import csv
import requests
from bs4 import BeautifulSoup

url ="https://kream.co.kr/social/tabs/style_discovery"
headers ={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

pictures = soup.find_all("div")

print(pictures)