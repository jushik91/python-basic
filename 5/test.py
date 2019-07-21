
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

##[함수 정의 형태]
# def 함수명(변수명):
#     명령문
#     return 값

##함수 정의
##함수 형태 : 매개변수 2개, Return값 없음
##함수 형태 : 매개변수 2개, Return값 없음
##단축키

def sum(a,b):
    s= a+b
    print(s)

##함수 호출
sum(3,5)
sum(2.1, 4.3)
sum('good', 'day')

def hello():
    print('hello~~~~!!!!')

##함수호출
hello()

##함수형태 : 매겨변수 1개, return 값 없음
def apple_count(apple):
    print('사과',apple)  ##한글처리가 안됨

apple_count(10)
