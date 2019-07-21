##print(help(input))
##사용자가 입력한 값의 2배된 갓을 출력
print('출력합니다.')
##num=int(input('정수하나를 입력해 주세요:'))
##print(type(num))
##print('num:', num*2)

##num2=float(input('실수하나를 입력하세요'))
##print(type(num2))
##print('입력받은 실수:', num2*2)


##문제
##su1,su2 변수 정수 2개를  입력 받아서 저정 -> 출력
##출력형태 : su1:10,su2:20

##su1=int(input('정수2개입력:'))
##su2=int(input())
##print('su1:{}, su2:{}'.format(su1,su2))
##print('su1:%d, su2:%d'%(su1,su2))

##숫자 데이타 1개를 이력(정수, 실수)

##su = eval(input('숫자데이타 한 개 입력 :'))
##print(type(su))
##print('su:', su)

##변수에 값 저장
##n1=10
##n2=20
##n1,n2=10,20
##print('n1:%d, n2:%d'%(n1,n2))

##하나의 input을 통해서 연속 입력된 값 저장
##s1,s2 = eval(input('숫자 2개를 입력 : '))
##print(type(s1))
##print('s1:{}, s2:{}'.format(s1,s2))


##하나의 input을 통해서 연속 입력된 값을 각 변수에  저장: 정수 형태로 !!
##d1,d2 = map(int, input('정수2개입력:').split(','))
##print(type(d1))
##print('d1:{}, d2:{}'.format(d1,d2))

##문자열 2개 이상을 입력받아 2개의 변수에 저장
##hi, hello를 각 변수에 저장
##s,t=input('문자열입력:')
##print(type(s))
##print('s:{}, t:{}'.format(s,t))

##hi, hello를 각 변수에 저장
##s,t=input('문자열입력:').split(' ')
##print(type(s))
##print('s:{}--문자수 :{}, t:{}-- 문자수{}'.format(s,len(s),t,len(t)))
##print
##

##de=int(input('10진수 입력:'))
##print('de: ' ,de)
##oct=int(input('10진수를 8진수로 변환'),8)
##print('oct(8진수): ' ,oct)
##hex = int(input('10진수를 16진수로 변환 :'), 16)
##print('hex(16진수):' , hex)

tuple_value = eval(input('값 입력(1,2,3): '))  ##tuple
print(tuple_value)
print(type(tuple_value))
print(tuple_value[0])


tuple_value = eval(input('값 입력[1,2,3]: '))  ##list
print(tuple_value)
print(type(tuple_value))
print(tuple_value[0])



  

print('완료')


