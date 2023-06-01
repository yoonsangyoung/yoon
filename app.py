from flask import Flask ,render_template , request
import csv
import os
from naver_stock import generate_csv_data
# from capture_practice import generate_capture

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")

def read_csv_data(filename):
    # csv 불러오기
    with open(filename, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def get_image_files():
    # 이미지 파일을 가져오는 코드
    image_folder = "static/images"  # 이미지 파일이 저장된 폴더 경로
    image_files = os.listdir(image_folder)
    return image_files

@app.route('/search')
def hello():
    keyword = request.args.get("keyword")
    print(keyword)
    if keyword == "조회":
        generate_csv_data()
        csv_data = read_csv_data("amount list.csv")
        return render_template("stock.html", keyword=keyword, data=csv_data)

    if keyword == "크림":
        image_files = get_image_files()
        return render_template("kream_image.html", images=image_files)