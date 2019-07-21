##사용자가 3을 넣으면 3단이 나온다
    
i=int(input('입력:'))

for n in range(1,10):        
    print('{}*{}={}'.format(i,n,int(n)*int(i))) 
    


##1~10까지 더하기

sum=0    
for n in range(1,11):
    sum +=n
print('{}'.format(sum))


## 1*2*3*4*5 결과 값

sum=1    
for n in range(1,6):
    sum *=n
print('{}'.format(sum))


## 자연수 1~100의  3의 배수를 리스트에 저장하고 갯수를 출력

##방법1
data=[]
for n in range(1,100):
    if n%3 ==0:
        data.append(n)
print('3의 배수:',data)
print('3의 배수 갯수:',len(data))
    

##방법2
data=[n for n in range(1,101) if n%3==0]
print('3의 배수:',data)
print('3의 배수 갯수:',len(data))



