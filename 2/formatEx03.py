##
print('%d'%15)
print('{}'.format(15))
fruit='apple'
count=10
print('제가 {0}를 {1}개 구입했습니다.'.format(fruit,count))
print('제가 {1}를 {0}개 구입했습니다.'.format(fruit,count))
print('제가 {1}를 {1}개 구입했습니다.'.format(fruit,count))

print('%d, %d, %d' %(count,count,count))
print('{0}, {0}, {0}'.format(count))
print('{0}'.format(2))    ##기본은 왼쪽 정렬
print('{0:5}'.format(2)) #5자리, 출력 자리수를 정해주면 오른쪽 정렬
print('{0:>5}'.format(2)) #5자리, >는 오른쪽 정렬  표시, 생략 가능
print('{0:<5}'.format(2))  #왼쪽 정렬을 위해서는 <표시함
print('{0:^5}'.format(2))  # ^는 가운데 정렬

print('{0:.2f}'.format(3.14152))


