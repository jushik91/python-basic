
##1.다음과 같이 코딩
score = {'hong': {'math':95, 'eng':85, 'kor':90},
             'park': {'math':85, 'eng':100, 'kor':80},
             'kim' : {'math':95, 'eng':85, 'kor':100}}
         
#[1.1] park의 모든 과목의 점수를 출력
print(score.get('park'))
print(score['park'])
#[1.1] kim의 kor 점수만 출력

temp=score.get('kim')
print(temp.get('kor'))
print(score['kim']['kor'])

         

##2. 다음과 같이 코딩

number =[100,200,100,500,200,600,300]
##[2.1]요소값에서 중복된 값을 제거하고 정렬하여 저장
##print('중복 제거된 number:',set(number))
number=list(set(number))
print(number)
print(type(number))

number.sort()
#[2.2] 요소값 300다음에 400을 추가하시오
##number.insert(3,400)
print('300의 인덱스:', number.index(300))
number.insert(number.index(300)+1,400)  ##List에서 Insert(넣어야할 곳의 위치, 넣을 값)
print(number)


##2. 다음과 같이 코딩

jumin='921103-1234567'

#[3.1]  년2자리 출력
print(jumin[0:2])
#[3.2]  월2자리 출력
print(jumin[2:4])
#[3.3]  일2자리 출력
print(jumin[4:6])
#[3.4] 성별 12자리 출력
print(jumin[7])
#[3.5] 11월을 8월로 변경하여 저장 : 920803-1234567'
print(jumin.replace('11','08'))



         
