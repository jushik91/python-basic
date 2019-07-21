##L= input()
##M=input()
##
##print(L)
##print(M)


##data=[]
##for n in range(2):
##    num= int(input())
##    data.append(num)  
##print(data)
##        
        

##하나의 input을 통해서 연속 입력된 값 저장
##s1,s2 = eval(input('숫자 2개를 입력 : '))
##print(type(s1))
##print('s1:{}, s2:{}'.format(s1,s2))

##
####하나의 input을 통해서 연속 입력된 값을 각 변수에  저장: 정수 형태로 !!
##d1,d2 = map(int, input('정수2개입력:').split(' '))
##print(type(d1))
##print('d1:{}, d2:{}'.format(d1,d2))


array_size = int(input())

array = list()

for i in range(array_size):
    array.append(int(input()))

array.sort()

for i in array:
    print(i)

