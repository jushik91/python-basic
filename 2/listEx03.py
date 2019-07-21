a = [1,2,3]
b = ['one','two','three']

print(a,b)
print(a+b)
print(a*3)

a[1]=5
print(a)

a[0:1]=[2,3,4] ##??
print(a)

a[0:1]=[]
print(a)

del a[1]
print(a)

a.sort()
print(a)

a.reverse()
print(a)

print(a.index(5))

a.append(7)
print(a)

a.insert(1,9)
print(a)

a.remove(9)
print(a)


##문제
##hi를 찾아서 Hello로 변경
data = [100,200,'hi','good',300]

print(data.index('hi'))
data[data.index('hi')]='hello'
print(data)
    
a=[1,2,['a','b',['life', 'is']]]
print(a[2][2][0])

a=[1,2,3]

print(str(a[2])+ 'hi')








