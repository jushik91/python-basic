## for 변수 in 여러 값:

data=[2,1,3]
for n in data:
    print(n)

for n in 'Hello':
    print(n)


## 범위를 변수에 담고 수행한다    
even = range(2,11,2)
for n in even:
    print(n,end ='')
    

##10에서 1가지 1씩 감소
for n in range (10,0,-1):
    print(n, end ='')

print("====")
##1에서 11까지 실행, 11인 제외 , 증가값은 2
for n in range (1,11):
    print(n, end ='')
    
##1에서 11까지 실행, 11인 제외 , 증가값은 2
for n in range (1,11,2):
    print(n, end ='')


##함수 인수에 1개만 입력 
for n in range (11):
    print(n, end ='')

## for문의 조건을 수행하고 왼쪽 명령문을 수행
## 1,2,3,4,5를 n에 놓고 오른쪽 조건을 수행하고 가장 왼쪽 print문 수행

[print(n) for i in range (1,6) if n%2==1]
##동일한 문
for n in range (1,6):
    if n%2 ==1:
        print(n)

data=[n for n in range (1,6)]  ##[]의 의미는 결과 n을 list에 넣는 것을 의미한다
print('data',data)


a=[(1,2),(3,4,),(5,6)]
print('a의 자료령:',type(a))
print('a[0]:',a[0])
##(a,b) = (10,20)
for n in a:
    print(n)
    

a=[(1,2),(3,4,),(5,6)]
print('a의 자료령:',type(a))
print('a[0]:',a[0])
##(a,b) = (10,20)
for n,m in a:
    print('n:{},m:{}'.format(n,m))



    
a=[(1,2),(3,4,),(5,6)]
print('a의 자료령:',type(a))
print('a[0]:',a[0])
##(a,b) = (10,20)
for n,m in a:
    print(n+m)
    
    
a=[(1,2),(3,4,),(5,6)]
print('a의 자료령:',type(a))
print('a[0]:',a[0])
##(a,b) = (10,20)
for n in a:
    print(n[0]+n[1])        


        
        




