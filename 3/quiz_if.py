##[quiz]
##[문제1] 사용자에게서 정수 1개를 입력 받아서 출력

a=input('정수를 입력 받자')
print(a)
print(type(a))

##[2] 사용자에게 정수 1개를 입력 받아서, 양수/음수/0 구분하여 출력

num=int(input('정수를 입력 받자'))
if num>0:
    print('양수')
elif num==0:
    print('0입니다')
else:                        ##else가 없어도 에러는 안남. 일반적으로 명시해야 함
    print('음수입니다')
  


##[3] 사용자에게 양의 정수 1개를 입력 받아어 짝수/홀수를 출력


num=int(input('정수를 입력 받자')) %2
if num==0:
    print('양수')
else:
    print('음수')
    

##[4] 사용자에게 정수 2개를 입력 받아서 , 큰 값 출력

    
##num1=int(input('정수를 입력 받자'))
##num2=int(input())
##if num1 >= num2:
##    print(num1)
##else:
##    print(num2)
    

##[5] 사용자에게 정수 1개를 입력 받아서, 해당되는 값의 법위를 출력
## 음수를 넣어주면 0미만의 수, 0이상 10미만의 수 , 10이상 20미만의 수,30 이상의 수

##num1 =int(input('정수를 입력 받자'))
##
##if num1 <0 :
##    print('0미만의 수')
##elif (num1>=0 and num1<10):
##    print('0이상 10미만의 수')
##elif (num1>=10 and num1<20):
##    print('10이상 20미만의 수')
##else :
##    print('30미만의 수')
##    


    
    


