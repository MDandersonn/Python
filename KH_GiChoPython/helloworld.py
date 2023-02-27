a=10
b=20
a,b= b, a+b  #=보다 +가 우선순위가 더 높아서 먼저실행됨
print(a,b)

print("hello world")#알트쉬프트위아래 :복사
print("hello world")#알트쉬프트위아래 :복사
#컨트롤 x :행삭제 (잘라내기기능)

#컨트롤 /  : 주석처리
#알트 위아래 :줄이동

a,b=100,200
print(a,b)

#False인경우 :빈문자,[],(),{},Null

#소문자>대문자 #첫문자의 아스키코드 기준.
print("a">"A")
print("62345">"123")
print("Python"<"python")

print("a" and 10>3 and True and 0 and False)#처음 False가 나오는 부분출력
print("a" and 10>3 and True and "aa")#모든결과값이 참이면 맨마지막꺼 출력

print(0 or 0.0 or False or "cham")#처음 참이 나오는 값을 출력.
print(True or False and "참") # and연산이 or연산보다 우선순위가 높아서 뒤부터 계산된다.
#false and  참의 결과인 false가 먼저 나오고  true or false 계산되니까 true가 출력됨
#우선순위를 지정해줄려면 () 안으로 싸면 된다.

print("{}".format(20*3))


text="www.google.com"
print(len(text))#내장함수
print(text.capitalize()) #메서드 
print(text)

numbers =1,2,3,4,5
n1,n2, *n3=numbers
print(n1)
print(n3)
print(type(n1))
print(type(numbers))