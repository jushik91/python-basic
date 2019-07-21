##5
##1 0 0 0 0
##0 1 1 1 1
##0 1 0 1 1
##0 0 0 0 1
##0 0 1 0 1

N=3

arr = [[1,0,0],[0,1,1],[0,0,1]]

for i in range(N):
    for j in range(N):
        print(arr[i][j],end=' ')
    print()

class Myclass(object):
    def __init__(self,number):
        self.number=number

my_object=[]
for i in range(100):
    my_object.append(Myclass(i))

#later

for obj in my_object:
    print (obj.number)


##2번째 방법
class YourClass(object) : pass
objs=[YourClass() for i in range(10)]
print(objs)
