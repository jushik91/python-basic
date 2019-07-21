import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

##함수정의
def say_myself(name,old,man=True):
    print("나의 이름은 %s입니다"%name)
    print("나이는 %d살입니다."%old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

##힘수호출
say_myself('박응용',27,True)
say_myself('박응용',27)
say_myself('박응용',27,False)


say_myself(man=False, name='이미자', old=35) ##순서를 안맞출려면 매개변수 이름을 직접 넣어준다
