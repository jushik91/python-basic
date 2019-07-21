#기본값 설정
#함수 형태 : 매개변수 1개, Return값 없음

# def default_func(arg=1):  ##arg 인수를 안넣을때 기본값으로 '1'을 쓰겠다
#     print('arg:', arg)
#
# default_func(100)
# default_func()


## 리턴값
## 기능 : 인수의 2배값을 리턴함

# def mul(num):
#     num *=2
#     return num
#
# result=mul(10)
# print('result:',result)

#문제
##div라는 함수를 정의하고 몱, 나머지 호출하시오
# def div(i,j):
#     return i//j
# re=div(10,3)
# print(re)


def div(i,j):
    if(j ==0):
        return 0 ,0
    else:
        return i//j , i%j
re=div(10,3)
print(re[0], re[1])
