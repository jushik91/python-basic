####튜플###

##리스트

a = [1,2,3]

##튜플 : 한번 선언된 요소의 값을 변경(삭제, 추가 변경) 할 수 없어요.

b= (1,2,3)

print('리스트: ',type(a))
print('튜플:',type(b))

a[0]=10
print(a)

##튜플은 이미 저장된 요소의 값을 변경할 수 없다
##b(0)=10
##print(b)

del a[0]
print(a)

##del b[0]
##print(b)


##튜플에서 인덱싱 가능
print(b[2])

#튜플에서 슬라이싱 가능

print(b[0:2])

#튜플 선언하는 방업
tuple1 =()
tuple2 =(1,) ##요소가 하나일때는 ,를 꼭 넣어야 한다
tuple3 =1,2,3 ## 여러개의 값을 넣을 때 자동으로 튜플로 인식
tuple4 = (1,2,3,(4,5,6))

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4))

a=1,2
print(type(a)) ## 튜플

a,b = 1,2
print(type(a)) ##

a = (1,2)
b = (3,4)

print(a+b)

print(a*3)











