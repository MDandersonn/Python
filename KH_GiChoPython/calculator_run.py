import calculator as cc
cc.add(50,40)
#저장을해야 컴파일됨!!!

from calculator import add, sub
add(22,11)
sub(22,11)

from datetime import date

today= date.today()
print(today)
new_date=date(1999,12,15)
print(new_date)

import datetime
print( datetime.time(9))

from datetime import time
print( time(5,2,2,4444))

from datetime import datetime
dt= datetime.now()
print(dt)

dt1= datetime(2002,10,20,14,5,2)
print(dt1)

from datetime import timedelta
print( dt - timedelta(days=20))# hours=20, wekks=24 등등 도가능

from time import localtime ,strftime
now= localtime()
print(now)

now1= strftime("%Y-%m-%d %H:%M")
print(now1)
now1= strftime("%Y년-%m월-%d일 %H시:%M분")
print(now1)
