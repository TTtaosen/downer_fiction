#encoding: utf-8
from bs4 import BeautifulSoup
import requests 
import os

def down_chapter(url):
    req = requests.get(url)
    req.encoding=('utf-8')
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div',id="content")
    return texts[0].text.replace('\xa0'*4,'\n\n')

def down_fiction(ufl):
    req = requests.get(url)
    req.encoding=('utf-8')
    html = req.text
    bf = BeautifulSoup(html)
    chapter_list = bf.find_all('div',id="list")
    ch_bf = BeautifulSoup(str(chapter_list[0]))
    chapter = ch_bf.find_all('a')
    for num in chapter:
        #print(url+"/"+num.get('href'))
        store_fiction(num.get('title'),down_chapter(url+"/"+num.get('href')))
        
def store_fiction(name,text):
    with open("三寸天堂.txt",'a',encoding='utf-8') as f:
        f.write(name+'\n')
        f.write(text)
if __name__=="__main__":
    url = "https://www.biquge.info/10_10582"
    print("downing 三寸天堂")
    down_fiction(url)
