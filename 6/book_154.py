
##전역변수 : Global 변수

a=1
def vartest(a):
    ##지역변수:함수 내에서 만든 변수, 매개변소도 지역 변
    num = 10
    a = a+1

vartest(a)
print(a)


##return을 사용한 함수값 변경
a1=2
def vartest2(a1):
    ##지역변수:함수 내에서 만든 변수, 매개변소도 지역 변
    a1 = a1+1
    return a1

a1=vartest2(a1)
print(a1)    ##라인삭제 shif+del


##전역변수를 사용한 함수값 변경
a3=5
def vartest3():
    ##지역변수:함수 내에서 만든 변수, 매개변소도 지역 변
    global a3
    a3 = a3+1

vartest3()
print(a3)    ##라인삭제 shif+del
