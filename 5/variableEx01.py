num=5  ##전역변수

def increment():    ##함수안의 지역변수는 함수빡에 선언됨 전역변수를 참조하지 못한다.
    global num ## 선언이므로 바로 값을 Assing하면 안된다.
    num = num+1
    print('inner num:',num)

increment()
print('outer num:',num)
