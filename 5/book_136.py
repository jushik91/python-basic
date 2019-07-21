
##하나의 input을 통해서 연속 입력된 값을 각 변수에  저장: 정수 형태로 !!

##
##t= int(input())



##방법 1
a=[1,2,3,4]
result=[]

for num in a:
    result.append(num*3)

print(result)

##방법 2  : 리스트 내포
result=[num*3 for num in a]
print(type(result))

for i in result:
    print(result,end='')


##방법 2  : 리스트 내포
result=[num*3 for num in a if num%2==0]
for i in result:
    print(result,end='')


##방법 2  : 리스트 내포
##result=[num=num+3 for num in a if num%2==0]  ##실행 단에는 대입(=)이 들어갈 수 없다
##for i in result:
##    print(result,end='')


result =[x*y for x in range(2,10)
                      for y in range(1,10)]

print(result)
