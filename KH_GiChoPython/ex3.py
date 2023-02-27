#super부모
#sub 자식
from pickletools import markobject


class ParentRestaurant:
    price=15000

    def __init__(self,name,menu,recipe):
        self.name= name
        self.menu=menu
        self.recipe=recipe

    def __str__(self):
        return "{},{},{}".format(self.name, self.menu, self.recipe)
    
    def __del__(self):
        pass

class ChildRestaurant(ParentRestaurant):#상속받을땐(부모클래스)추가
    price=20000 #(재정의. 즉 오버라이딩)
    #marketing="온라인마케팅"
    def __init__(self, name ,menu, recipe,marketing):
        ParentRestaurant.__init__(self, name, menu, recipe)
        self.marketing=marketing
    def __str__(self):
        return super().__str__() + ", {}".format(self.marketing)

#하위클래스가 상위클래스의 모든속성을 갖게된다.
#restaurant_info=ChildRestaurant("자식가게","붕어빵","붕어빵굽는다")
#print(restaurant_info)
#print(restaurant_info.price)#상위클래스!에서정의된속성을 고쳐서 재정의 (오버라이드)
#!print(restaurant_info.marketing)

restaurant_info2=ChildRestaurant("자식가게", "붕어빵", "붕어빵굽는다", "마케팅할껴")
print(restaurant_info2)

print(issubclass(ChildRestaurant,ParentRestaurant)) #하위클래스인지 확인하는 함수
