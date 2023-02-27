import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.naver.com/")
#print(r)#200이면 ok
#print(r.content)# 16비트
#print(r.text)#알아볼 수 있는 형태

bs=BeautifulSoup(r.content, "html.parser")
#print(bs)#파이썬이 이해할 수있게 파싱을 해줘야함
'''
h3=bs.select("h3") #리스트형
print(h3)


#print(h3.text) #인덱싱이 지정이안되면 에러
print(h3[1].text)

print(h3[0].name)# 태그네임
print(h3[0].attrs)#태그의 속성과 값

h3=bs.select_one("h3") #리스트의 맨 앞
print(h3)

print(h3.text)

h3=bs.select_one("h3 > a")
print(h3)

h3=bs.select("div.current_box")
print(h3)

h3=bs.select(".title")
print(h3)

h3=bs.select("#u_skip")
print(h3)
'''
# h3=bs.find_all("h3",{"속성명"}:값) #리스트형
h3=bs.find_all("div",{"class":"partner_box"})
print(h3)

'''
print(123123123123)
h3=bs.find("div",{"class":"partner_box"})#가장 첫번째 요소출력
print(h3)
print(h3.text)
'''
