import requests
from bs4 import BeautifulSoup
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}


url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'


res = requests.get(url, headers = headers)


soup = BeautifulSoup(res.content, 'html.parser')


data = soup.select('span.item_title')

i = 0
final = []

for item in data:
    item_1 = item.get_text()
    final.insert(i,item_1)
    i = i + 1
    


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}


url = 'https://zum.com/#!/home'


res = requests.get(url, headers = headers)


soup = BeautifulSoup(res.content, 'html.parser')


data = soup.select('span.keyword.d_keyword')


i = 0
final_1 = []

for item in data:
    item_1 = item.get_text()
    final_1.insert(i,item_1)
    i = i + 1



chrome_options = Options()
chrome_options.binary_location = r"/usr/bin/google-chrome"
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage') 
driver = webdriver.Chrome(options=chrome_options, executable_path=r'/home/ubuntu/projects/myproject/chromedriver')
driver.get("https://trends.google.co.kr/trends/?geo=KR")
req = driver.page_source
soup = BeautifulSoup(req,'html.parser')

data = soup.select('div.list-item-title')

final_2 = []
i = 0

for item in data:
    item_1 = item.get_text()
    final_2.insert(i,item_1)
    i = i + 1



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}


url = 'https://www.melon.com/chart/index.htm'

res = requests.get(url, headers = headers)

soup = BeautifulSoup(res.content, 'html.parser')

data = soup.select('div.ellipsis.rank01 > span > a')


i = 0
final_3 = []

for item in data:
    item_1 = item.get_text()
    final_3.insert(i,item_1)
    i = i + 1



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

url = 'https://www.genie.co.kr/chart/top200'

res = requests.get(url, headers = headers)

soup = BeautifulSoup(res.content, 'html.parser')

data = soup.select('a.title.ellipsis')


i = 0
final_4 = []

for item in data:
    item_1 = item.get_text()
    final_4.insert(i,item_1)
    i = i + 1

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}


url = 'https://music.bugs.co.kr/'


res = requests.get(url, headers = headers)


soup = BeautifulSoup(res.content, 'html.parser')


data = soup.select('th > p.title > a')



i = 0
final_5 = []

for item in data:
    item_1 = item.get_text()
    final_5.insert(i,item_1)
    i = i + 1







main = Blueprint('main', __name__, url_prefix='/')
@main.route('/',methods=['GET'])
def index():
    return render_template('/main/main.html')
@main.route('/inproduct',methods=['GET'])
def inpro_1():
    return render_template('/inpro/inpro.html')
@main.route('/inmo', methods=['GET'])
def inmo_1():
      naverdata1 = final[0]
      naverdata2 = final[1]
      naverdata3 = final[2]
      naverdata4 = final[3]
      naverdata5 = final[4]
      naverdata6 = final[5]
      naverdata7 = final[6]
      naverdata8 = final[7]
      naverdata9 = final[8]
      naverdata10 = final[9]

      zumdata1 = final_1[0]
      zumdata2 = final_1[2]
      zumdata3 = final_1[4]
      zumdata4 = final_1[6]
      zumdata5 = final_1[8]
      zumdata6 = final_1[10]
      zumdata7 = final_1[12]
      zumdata8 = final_1[14]
      zumdata9 = final_1[16]
      zumdata10 = final_1[18]

      googledata1 = final_2[0]
      googledata2 = final_2[1]
      googledata3 = final_2[2]
      googledata4 = final_2[3]
      googledata5 = final_2[4]
      googledata6 = final_2[5]
      googledata7 = final_2[6]
      googledata8 = final_2[7]
      googledata9 = final_2[8]
      googledata10 = final_2[9]


 

      melondata1 = final_3[0]
      melondata2 = final_3[1]
      melondata3 = final_3[2]
      melondata4 = final_3[3]
      melondata5 = final_3[4]
      melondata6 = final_3[5]
      melondata7 = final_3[6]
      melondata8 = final_3[7]
      melondata9 = final_3[8]
      melondata10 = final_3[9]

      geniedata1 = final_4[0]
      geniedata2 = final_4[1]
      geniedata3 = final_4[2]
      geniedata4 = final_4[3]
      geniedata5 = final_4[4]
      geniedata6 = final_4[5]
      geniedata7 = final_4[6]
      geniedata8 = final_4[7]
      geniedata9 = final_4[8]
      geniedata10 = final_4[9]
      
      bugsdata1 = final_5[0]
      bugsdata2 = final_5[1]
      bugsdata3 = final_5[2]
      bugsdata4 = final_5[3]
      bugsdata5 = final_5[4]
      bugsdata6 = final_5[5]
      bugsdata7 = final_5[6]
      bugsdata8 = final_5[7]
      bugsdata9 = final_5[8]
      bugsdata10 = final_5[9]
      
      
      


      return render_template('/inmo/table.html', naverdata_1=naverdata1,naverdata_2=naverdata2,naverdata_3=naverdata3,naverdata_4=naverdata4,naverdata_5=naverdata5,naverdata_6=naverdata6,naverdata_7=naverdata7,naverdata_8=naverdata8,naverdata_9=naverdata9,naverdata_10=naverdata10,
      zumdata_1=zumdata1,zumdata_2=zumdata2,zumdata_3=zumdata3,zumdata_4=zumdata4,zumdata_5=zumdata5,zumdata_6=zumdata6,zumdata_7=zumdata7,zumdata_8=zumdata8,zumdata_9=zumdata9,zumdata_10=zumdata10,
      googledata_1=googledata1,googledata_2=googledata2,googledata_3=googledata3,googledata_4=googledata4,googledata_5=googledata5,googledata_6=googledata6,googledata_7=googledata7,googledata_8=googledata8,googledata_9=googledata9,googledata_10=googledata10,
      melondata_1=melondata1, melondata_2=melondata2, melondata_3=melondata3, melondata_4=melondata4, melondata_5=melondata5, melondata_6=melondata6, melondata_7=melondata7, melondata_8=melondata8, melondata_9=melondata9, melondata_10=melondata10,
      geniedata_1=geniedata1, geniedata_2=geniedata2, geniedata_3=geniedata3, geniedata_4=geniedata4, geniedata_5=geniedata5, geniedata_6=geniedata6, geniedata_7=geniedata7, geniedata_8=geniedata8, geniedata_9=geniedata9, geniedata_10=geniedata10,
      bugsdata_1=bugsdata1, bugsdata_2=bugsdata2, bugsdata_3=bugsdata3, bugsdata_4=bugsdata4, bugsdata_5=bugsdata5, bugsdata_6=bugsdata6, bugsdata_7=bugsdata7, bugsdata_8=bugsdata8, bugsdata_9=bugsdata9, bugsdata_10=bugsdata10
      )
    
