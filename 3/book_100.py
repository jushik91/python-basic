import sys 

print(sys.getrefcount(3))  ##3을 참조하는 변수의 갯수를 가져온다
##파이션은 주소를 출력할 수 없다
## C언어는 주소를 출력할 수  있다.
## Java는 주소를 변환해서 보여준다.


a=3
b=3

print(sys.getrefcount(3))

print(a is b)


## 변수 a는 3을 가리킨다
## 변수 a는 3을 참조한다


