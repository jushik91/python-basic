##문제 5
##60점 이상인 학생번호와 점수 출력
##학생번호 : 1,2,3,4,5


##방법1
math=[90,45,60,75,50]

idx=1

for m in math:
    if m>= 60 :
        print('{}번째 학생은 {}점'.format(idx,m))
        idx +=1
##[방법2]
for m in range(len(math)):
    if math[m]>=60:
        print('{}번째 학생은 {}점 '.format(m+1,math[m]))


##방법3
for idx,m in enumerate(math,1):  ## idx에 변수를 만듬
    print('idx:{},m:{}'.format(idx,m))

for idx,m in enumerate(math):  ## idx에 변수를 만듬
    if m>60:
        print('idx:{},m:{}'.format(idx,m))

##############문제 6######################
##방법1
        
math={'일길동':90,'이길동':45, '삼길동':60,'사길동':75,'오길동':50}
for key in math:  ##m에 저장되는 것은 dictionary의 key값    
    if math[key]>= 60 :
        print('{}번째 학생은 {}점'.format(m,math[key]))

for v in math.items():
    print(v)
    print(type(v))


for key,value in math.items():
    if value >=60:
        print('{} 학생은 {}점'.format(key,value))
        
              

for data in math.items():
    if data[1] >=60:
        print('{} 학생은 {}점'.format(data[0],data[1]))
        

              
              

        
    
    
   

