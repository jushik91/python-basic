
a=[(1,2),(3,5),(5,6)]
for first,last in a:
    print('first:{}, last:{}'.format(first,last))


for first in a:
    print(first)
    print('first:{}, last:{}'.format(first[0],first[1]))
    
    
marks=[90,25,67,45,80]
number =0
for mark in marks:
    number = number +1
    if mark >=60:
        print('%d번 학생은 합격입니다. '%number)
    else:
        print('%d번 학생은 불합격입니다.'%number)

        

for numbers, mark in enumerate(marks,1):     ## enumberate에 만든 순서값이 첫번째 변수, 1은 시작값
    if mark >=60:
        print('%d번 학생은 합격입니다. '%numbers)
    else:
        print('%d번 학생은 불합격입니다.'%numbers)


for number, mark in enumerate(marks,1):     
    if mark < 60:
        continue
    print('%d번 학생은 합격입니다. '%number)
    
##[p133]
    a= range(10) #0~9
    print(a)

##[p133]
marks=[90,25,67,45,80]

for number in range(len(marks)):
    if marks[number] <60:
        continue
    print('%d번학생은 합격입니다.'%(number+1))













