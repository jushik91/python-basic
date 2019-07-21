#1.re 모듈 import


import re

data='abc d2y mart food day 3 7 9'

#2. compile(정규표현식)

#p=re.compile('[m]')
#p=re.compile('[bc]')
#p=re.compile('[a-z]')
#p=re.compile('[a-zA-Z]')

#p=re.compile('[0-9]')

#p=re.compile('[a-zA-Z0-9]')##알파벳 및 숫자전부를 찾는다

#p=re.compile('[135]')

#p=re.compile('[^135]') ##135를 제외한 나머지 모두를 찾아라


#p=re.compile('[\d]')  ##0에서 부터 9

#p=re.compile('[\D]')  ##[^0-9]

#p=re.compile('[\s]')

#p=re.compile('[a.b]')
#p=re.compile('[a].b')
# p=re.compile('abc')
# p=re.compile('day')

#p=re.compile('d.y')

#p=re.compile('fo*d')  ##별표는 반복, 없어도 됨
#p=re.compile('fo+d') ##o가 한번 이상은 반복이 되어야
#p=re.compile('fo{2}d')

p=re.compile('[a-z]+')
#p=re.compile('[a-z]')



#3. 검색 함수

print('match : ', p.match(data))
print('search: ', p.search(data))
print('findall: ', p.findall(data))
print('finditer: ', p.finditer(data))  #span은 위치를 알려줌. 앞에 것이 index

for d in p.finditer(data):
    print(d)


m=p.match(data)
print('group:', m.group())
print('start:', m.start())
print('end:', m.end())
