##

def sum(a,b):
    return a+b
def safe_sum(a,b):
    if type(a) !=type(b):
        print('더할수 있는것이 아니다')
        return ## 함수 실행 종료

    else:
        result = sum(a,b)

    return result

if __name__=='__main__':
    print(safe_sum('a',1))
    print(safe_sum(1,4))
    print(sum(10, 10.4))
