from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

before_url = 'http://www.kyobobook.co.kr/product/productSimpleReviewSort.laf?gb=klover&barcode=9788901243665&ejkGb=KOR&mallGb=&sortType=like'

barcodes = ['9791186757093']

url = 'http://www.kyobobook.co.kr/product/productSimpleReviewSort.laf?gb=klover&barcode='
# webpage = urlopen(url)
#
# source = BeautifulSoup(webpage, 'html5lib')
# reviews = source.find_all('div', {'class': 'txt'})

# for review in reviews:
#     print(review.get_text().strip())

driver = webdriver.Chrome('chromedriver.exe')
delay_time = 1

file = open('book_2018.txt','w', encoding="utf-8")

for j in barcodes:
    url2 = 'http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode='+j
    url = 'http://www.kyobobook.co.kr/product/productSimpleReviewSort.laf?gb=klover&barcode=' + j + '&ejkGb=KOR&mallGb=&sortType=like'
    driver.implicitly_wait(delay_time)
    webtotal = driver.get(
        url2+'#review')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1', {'class': 'title'}).getText()
    title = title.split('\n')[5]
    title = title.strip()
    print(title)
    # source2 = BeautifulSoup(html, 'html5lib')
    # result = source2.find('span', {'class':'kloverTotal'}).getText()
    driver.implicitly_wait(delay_time)
    webtotal = driver.get(
        url2+'#review')
    html = driver.page_source
    driver.implicitly_wait(delay_time)
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find('span', {'class': 'kloverTotal'}).getText()
    result = result.replace('(', '')
    result = result.replace(')', '')
    result = int(result)
    print(result)
    for i in range(1, int(result / 5) + 1):
        total_url = url+ '&pageNumber=' + str(i) +"&orderType=order"
        webpage = urlopen(total_url)
        source = BeautifulSoup(webpage, 'html5lib')
        reviews = source.find_all('div', {'class': 'txt'})
        for review in reviews:
            comment = review.get_text().strip()
            comment = comment.replace('\n','')
            file.write(title+'\t')
            file.write(j+'\t')
            file.write(comment)
            file.write("\n")
file.close()