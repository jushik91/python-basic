a = {1:'hi', 2:'hello', 'name':['kim','park','Lee'], 1:'good'} ##키가 중복되면 1개는 random하게 무시된다,
##리스트는 키값으로 사용할 수 없다. 튜플은 키값으로 사용 가능하다.

print(a[1])
print(a['name'])  ##list가 나온다
print(a['name'][1])

a[3]='b'
print(a)
print(a.keys())

for k in a.keys():
    print('출력:',k)

print(a.items())
it=list(a.items())
print(type(it[0]))
print(it[0])

print(a.get('addr', 'default'))
