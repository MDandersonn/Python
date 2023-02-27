import requests;
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup;
inp= input("검색어를 입력하세요: ")
r= requests.get("https://news.google.com/search?q=" +inp+"&hl=ko&gl=KR&ceid=KR%3Ako")
bs= BeautifulSoup(r.content, "html.parser")

b=bs.find_all("div",{"class":"j7vNaf"})
news=[]
for i in b:
    title = i.find("h3").text
    links = "https://news.google.com"+i.find("a")['href'][1:]
    # article= i.find("span",{"class":"xBbh9"}).text
    time =i.find("time").text
    news.append([title,links,time])

result=pd.DataFrame(news, columns=["기사","링크","시간"])
print(result)
result.to_excel('news.xlsx')


# b=bs.select("h3.RD0gLb > a ")
# print(b[0].text)!
# print(b[0].attrs['href'][1:])


# news=[]
# for i in range(len(b)):
#     news.append([b[i].text, "https://news.google.com"+b[i].attrs['href'][1:]])

# result=pd.DataFrame(news, columns=["기사","링크"])
# print(result)
# result.to_excel('news.xlsx')


