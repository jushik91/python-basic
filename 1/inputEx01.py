#age=input("나이를 입력해 주세요")
#age2=input("나이를 2번째입력해 주세요")

##print( age)
##print( age2)

for x in range(2):
    print(x)


lst = [0,0,0,'a','6','7']
print(lst)
sst = ['i','am', 'a', 'key']

print(sst)


est = []
print(est)
numbers = [1,2,3,4,5]
print('첫번째 값 : %d'%numbers[0])
print('두번째 값 : %d'%numbers[1])
print('numbers 길이 : %d'%len(numbers))
print('lst 길이 : %d'%len(lst))

##for i in range(0,5,1):
##    n = int(input('index %d :'%i))
##    numbers[i]=n
print("nubmers=", numbers)
print(numbers[2:4])

zete = [0,1,2,3,4,5]
tetw = [10,11,12,14,14]
twth = [20,21,22,23,24]

allNumbers =[zete,tetw,twth]

print('일차원',zete,tetw,twth,'\n')
print('이차원', allNumbers)
print(allNumbers[1][1])


n=10
arr = []
for  i in range(10):
    arr.append(0)
print(arr)

n=10
arr=[7 for i in range(2,7,2)]
print(arr)


##arr[7 for i in range(1,5,1)]
##print(arr)

N,M = 5,3
arr = []
for i in range(N):
    tmp =[]
    for j in range(M):
        tmp.append(0)
    arr.append(tmp)

print(arr)    
print("*"*30)
N,M = 5,3
arr = []
for i in range(N):
    arr.append([0 for j in range(M)])
print(arr)

N,M= 5,3
arr=[[0 for j in range(M)] for i in range(N)]
print(arr)

print("="*30)
N,M = 5,3
arr=[]
for i in range(N):
    tmp=[]
    for j in range(M):
        tmp.append(0)
    arr.append(tmp)   

print(arr)

##1 2 4
##3 2 5

arr=[[1,2,4],[3,2,5]]
arr1=[(1,2,4),(3,2,5)]
print(arr[1][1])
print(arr1[1][1])     
 
##함수
print("함수 예제")
def sum(a,b):
    s = a + b
    return s
total = sum(4,7)
print(total)

def f(i,mylist):
    i=i+1
    mylist.append(0)
k=0
m=[1,2,3]

f(k,m)
print(k,m)

i=1
while i<10:
    print(i)
    i+=1

sum=0
for i in range(10):
    sum +=i
print(sum)

list = ['This', 'is', 'the', 'Sunday']
for i in list:
    print(list)

numbers= range(2,11,2)
for i in numbers:
    print(i)
 
    
class MyClass:
    pass

class Rectangle:
    count=0
    def __init__(self,width,height):
        self.width=width
        self.height=height
        Rectangle.count +=1

    def calcArea(self):
        area=self.width*self.height
        return area

    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth==rectHeight

    @classmethod
    def printCount(cls):
        print(cls.count)

##테스트
square = Rectangle.isSquare(5,5)
print(square)

rect1 =  Rectangle(5,5)
rect2 =  Rectangle(2,5)
print(rect1.printCount())


    
        





    











