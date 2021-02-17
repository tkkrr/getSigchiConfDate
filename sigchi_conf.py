from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Chromeをバックグラウンドで実行する設定
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome("./chromedriver", options=options)

# 動的ページなので，表示されるまで少々待ってHTMLを取得
driver.get('https://programs.sigchi.org')
time.sleep(1)
html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

conf_names = soup.select('h3.name')
conf_dates = soup.select('p.date')

# 10件表示してくれるスクリプト
for i in range(min(10, len(conf_names))):
    name = conf_names[i].get_text()
    name = name[:name.find(" :")]
    print(f"{name} : {conf_dates[i].get_text().strip()}")