from copy import copy  ## 피이선은 모듈이라고 한다

##a,b = 'python','life'
## 원래는  (a,b) = ('python','life')의 의미임

a=b='python'

print('a:',a)
print(type(a))

print('b:',b)
print(type(b))


n1=3
n2=5
print('n1:{}, m2:{}'.format(n1,n2))

n1,n2 = n2,n1   ##파이션은 두변수의 값을 바꾸는 것이 1줄로 가능 !!!!!!

print('n1:{}, m2:{}'.format(n1,n2))

del(n1)   ##  n1이라는 변수를 지운다
##print(n1)   ## 변수를 지운후 프린트하면 에러가 난다

######### 주소를 복사한다
lst1 = [1,2,3]
lst2 = lst1

lst1[1]=200

print('lst1:',lst1)
print('lst2:',lst2)

########## 데이타를 복사한다 : 방법1
lst1 = [1,2,3]
lst2 = lst1[:]

lst1[1]=200

print('lst1:',lst1)
print('lst2:',lst2)

########## 데이타를 복사한다 : 방법2
lst1 = [1,2,3]
lst2 = copy(lst1)

lst1[1]=200



print('lst1:',lst1)
print('lst2:',lst2)
print(lst1 is lst2)



