class BreadMold:
    #속성:일반적인변수
    category = "빵"

    def __init__(self):
        ##__init__생성자 메서드 :객체가생성될때 자동으로실행되는 메서드
        print("빵을만들었습니다")

    def make_bread(self):
        print("빵을 만들어낸다")


#객체이름 = 클래스이름()<<-이건 생성자라고부름
bread = BreadMold() #클래스를이용해서만든 객체를 인스턴스라고함.
bread.price = 3000
print(bread.category)
print(bread.price)

bread_choco =BreadMold()
bread_choco.category="초코 크림빵"
print(bread_choco.category)

bread.make_bread()#에러
#인스턴스의 메서드를 호출할때는 암묵적으로 ()안에 인자로 인스턴스가 들어가게된다
#그래서 def 정의할떄 self라고 넣어야함.

bread1=BreadMold()
bread2=BreadMold()
bread3=BreadMold()
print(bread1.category,bread2.category,bread3.category)
print( id(bread2.category) )
bread2.category="붕어빵"
print( id(bread2.category) )
bread2.category="붕어빵빵"
print( id(bread2.category) )

#dir() 이름공간에있는 모든 속성을 리스트로 반환
print(dir(bread1))

##__init__생성자 메서드 :객체가생성될때 자동으로실행되는 메서드
bread4= BreadMold()
