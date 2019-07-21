a=[1,2,3]

print(type(a))
print(a)
a[2]=4

print(a)

## 주석처리 : alt+3
##print(a[1:2])

##print('a[1:2]자료형: ',type(a[1:2]))
##print('a[1]자료형: ',type(a[1]))

a[1:2]=['a','b','c']
print(a)

a[1]=['a','b','c']
print(a)

a[1:3]=[]
print(a)

del a[1]
print(a)

a.append(6)
print(a)

a.append([5,6])
print(a)


##han=['황','박','김']
##print(han)
##han.sort()
##print(han)


##요소삭제
del a[3]
print(a)

##요소 추가
a.append(3)
print(a)

a.sort() ## 오름차순 정렬
print(a)

a.reverse()  ##오름찬순하고 내림차순으로 정렬한다.
print(a)

idx=a.index(4)
print("요소위치:",idx)

## a.insert(인덱스, 값)
a.insert(0, 10)
print(a)
a.append(4)
print(a)

##a.remove(4) 리스트이의 값을 지운다, 첫번째 왼쪽 것을 지원다
a.remove(4)
print(a)

##a.pop() 가장 끝의 있는 것을 가져온다  (인덱스) 인덱스값을 넣으면 인덱스 0의 값을 꺼내온다
del_val = a.pop(0)
print('삭제된 데이타 :', del_val)
print(a)

cnt=a.count(3)
print('요소 3의 갯수:',cnt)

print('리스트a의 요소 갯수:', len(a))
##a.extend([20,30])
a+=[20,30]
print(a)





