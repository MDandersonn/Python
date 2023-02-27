from urllib import request
import requests
from bs4 import BeautifulSoup
user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
hrd={'User-Agent':user_agent}
r=requests.get("https://www.melon.com/chart/", headers=hrd)
bs=BeautifulSoup(r.content, "html.parser")
bs=BeautifulSoup(r.text, "html.parser")
#print(bs)
songList=[]
singerList=[]
song=bs.select("div.rank01 > span > a") #클래스명이 띄어쓰기이면 뒤에꺼만 작성
#a=bs.find_all("div",{"class":"ellipsis rank01"})
singer=bs.select("div.rank01 > span > a")

for i in range(len(song)):
    songList.append(song[i].text)
    singerList.append(singer[i].text)
    print(f"순위 : {i+1}  제목 : {songList[i].strip()}  가수명: {singerList[i].strip()}")