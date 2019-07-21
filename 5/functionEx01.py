##함수 형태 : 가변변수 (가변인자), 리턴값 없음
## 함수(기능, 동작): 인수의 총합을 계산하여 출력

def sum(a,b, *args):  ##*한개는 tuple로 받은다는 것을 의미함 . 포인터가 아님
    result = a+b
    for n in args:
        result = result +n
    print('sum:',result)
    args = list(args)  ##다른 변수명 가능
    args.append(10)
    print('args:', args)



##함수 호출
sum(3,4,5,7)  ##19
sum(3,4)      ##7
