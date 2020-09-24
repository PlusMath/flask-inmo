import requests
# bs4 라 불리는 html 분석 라이브러리
from bs4 import BeautifulSoup

# 유저 설정
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

# 네이버 메인이 아닌 DataLab 페이지
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'

# User 설정
res = requests.get(url, headers = headers)

# res.content 주의
soup = BeautifulSoup(res.content, 'html.parser')

# span.item_title 정보를 선택
data = soup.select('span.item_title')

i = 0
final = []
# for 문으로 출력해준다.
for item in data:
    item_1 = item.get_text()
    final.insert(i,item_1)
    i = i + 1


from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
# 추가할 모듈이 있다면 추가


main= Blueprint('main', __name__, url_prefix='/')
@main.route('/main', methods=['GET'])
def index():
      naverdata = final[0]
      # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
      return render_template('table.html', naverdata_1 = naverdata)





