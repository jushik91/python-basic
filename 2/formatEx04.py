##서식 문자 :  %c
##문자코드표 : 아스키코드 (ASCII)

ch=98
print('문자값: %c'%ch)
#print('문자값: %s'%ch)
print("%-10s|jane"% 'hi')

fruit = 'apple'
count = 10
print('제가 {}를 {} 개 구입했습니다'.format(fruit,count))
print('제가 {0}를 {1} 개 구입했습니다'.format(fruit,count))
print('제가 {a}를 {b} 개 구입했습니다'.format(a=fruit,b=count))
print('제가 {0}를 {b} 개 구입했습니다'.format(fruit,b=count))
print('{0:<10}'.format("hi"))
print('{0:10}'.format('hi'))
print('{0:>10}'.format('hi'))
print('{0:^10}'.format('hi'))

print('{0:!<10}'.format("hi")) #{} 중괄호 Format함수g은 원하는 거승ㄹ 아무거나
print('포맷함수는 {{}}를 사용합니다.'.format())



