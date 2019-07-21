import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#함수정의
def sum_and_mul(a,b):
    return a+b, a*b

##함수호출

result = sum_and_mul(3,4)
print(result)
print(type(result))  ##라인복사  ctrl+shift+D


result1,result2 = sum_and_mul(3,4)
print(result1,result2)
print(type(result1))

def say_nick(nick):
    if nick=='바보':
        return
    print('나의 별명은 %s입니다'%nick)

say_nick('야호')
say_nick('바보')
