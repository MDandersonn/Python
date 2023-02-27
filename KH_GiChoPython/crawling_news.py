import requests;
import openpyxl
import pandas as pd
from bs4 import BeautifulSoup;
r= requests.get("https://news.google.com/search?q=%EC%88%98%EB%A6%AC%EB%82%A8&hl=ko&gl=KR&ceid=KR%3Ako")
bs= BeautifulSoup(r.content, "html.parser")

b=bs.select("h3.RD0gLb > a ")
print(b[0].text)
print(b[0].attrs['href'][1:])


news=[]
for i in range(len(b)):
    news.append([b[i].text, "https://news.google.com"+b[i].attrs['href'][1:]])

result=pd.DataFrame(news, columns=["기사","링크"])
print(result)
result.to_excel('news.xlsx')


