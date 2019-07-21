list1 = [1,2,3]

s1 =set([1,2,3,1])    ##set이라는 자료형으로 바꾼다는 의미
print(s1)
print(type(s1))


s2 = set('Hello')
print(s2)
print(type(s2))


s1.add(4)  ## add는 한값만 추가 가능
print(s1)

s1.update([4,5])   ##여러개의 값은 update를 쓴다
print(s1)

s1.remove(2)   ##특정 값을 지운다
print(s1)

#####################
s1 = set([1,2,3,4])
s2 = set([1,2,5,6])

##교집합
print('교집합:',s1&s2)
print('교집합:',s1.intersection(s2))

##합집합
print('합집합:',s1 | s2)
print('합집합:',s1.union(s2))

##차집합

print('차집합:',s1- s2)
print('차집합:',s1.difference(s2))
