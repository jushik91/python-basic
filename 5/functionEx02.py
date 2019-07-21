
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

## 함수 형태 : 가변변수, 리턴값 없음
##예제1
def student_score(**score):  ##**가 2개이면 여러개 인수를 받는데, Dictionary형식으로 받음
    n_cnt=0
    sum=0
    for i in score.keys():
        print(i,score[i])
        sum += score[i]
    print('총점:',sum)
    print('평균:',sum/len(score))



##함수호출
student_score(kor=100, eng=95, math=90) ## 인수롤 넣을때는 이렇게


##예제2
def student_score2(**score):  ##**가 2개이면 여러개 인수를 받는데, Dictionary형식으로 받음
    sum=0
    for key,value in score.items():
        print(key,value)
        sum=sum+value ##누적합

##함수호출
student_score2(kor=100, eng=95, math=90) ## 인수롤 넣을때는 이렇게

#dic = {'name' : 'park'}
