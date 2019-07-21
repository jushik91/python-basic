a = [1,2]
b = [3,4]

print(a+b)
print(a*3)

#a = a*3
a *=3

print(a)
a[1]=100
print(a)
a[2:4]=[200,300]
print(a)
a[2:4]=[]
print(a)
a[0]=50
print(a)
del a[0]
print(a)

a.sort()
print(a)

a.reverse()  ##내림차순시는 먼저 오름차순을 반드시 먼저 한다
print(a)

a=['one','two','three']
print(a.index('two'))

a.append(100)
print(a)
a=a+[200,300]
print(a)
a.insert(3,'four')
print(a)

a.remove('two')

print(a)

print(a.pop())
print(a)

print(a.pop(1))
print(a)

print(a.count(100))

a.extend(b)
print(a)




