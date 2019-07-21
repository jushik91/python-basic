##생성자정의
##객체생성시, 무조건 자동으로 호출
##생성자는 함수
##이름이 정해져 있음:Dog__init__
##2개 이상의 생성자를 정의xxx
##생성자를 명시하지 않으면
## 매개변수가 없는 하는일이 없는
## 생성자를 자동으로 추가
   # __init__(self):
   #     pass

##생성자는 객체를 생성할때 자동으로 변수값을 할당을 원할때 사용

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Service:
    secret="영구는 배꼽이 두개다"
    def __init__(self,name):
         self.name=name

    def setname(self,name):
        self.name = name

    def sum(self,a,b):
        result= a+b
        print('%s님 %s +%s =%s입니다.:'%(self.name,a,b,result))


pey=Service('홍길동1')
#pey.setname('홍길동2')
pey.sum(1,1)
