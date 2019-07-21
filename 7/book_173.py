result=0

def adder(num):
    global result  ##global 옆에 바로 값 설정 하면 안됨
    result +=num
    return result

print(adder(3))
print(adder(4))
