#__init__ 생성자 메서드 (초기값을넣어준다는의미)
# __del__ 소멸자 메서드(객체가 소멸될때 실행되는거)
class BreadMold:
    #속성:일반적인변수
    category = "빵"

    def __init__(self,category1,price1):
        ##__init__생성자 메서드 :객체가생성될때 자동으로실행되는 메서드
        print("빵을만들었습니다")
        self.category=category1
        self.price=price1#객체가 생성될때 매개변수를 갖는 생성자.

    def __del__(self):
        print("빵이 없어졌습니다")
        #프로그램실행이 종료되면 객체도 소멸함.
        #참조하고있는 객체를 객체변수들이 더이상 참조하고있지않을때 실행.
    def __str__(self):
        #객체를 문자열로 출력을 했을때  객체의 주소 대신 반환값을 지정해서 호출됨.
        return "hello"

    def make_bread(self):
        print("빵을 만들어낸다")
    

bread1=BreadMold("붕어빵",3000)#이객체를 참조하는변수가없으면 레퍼런스카운트가0 . 그래서 소멸자메소드가 실행됨
bread1= BreadMold("빵",1000)#bread1이 참조하는 객체가 변함.그래서 위에꺼 소멸.
print(bread1.price)

print(bread1)