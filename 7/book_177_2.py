import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Service:
    secret="영구는 배꼽이 두개다"
    def sum(self,a,b):
        self.result = a+b   ##인스턴수 변수로 선언하면 다른 함수에서 사용 가능
        print("%s + %s = %s입니다."%(a,b,self.result))

    def func(self):
        print('덧셈결과:',self.result)

pey=Service()

##두가지 방법 다 가능

print(pey.secret)
print(Service.secret)

pey.sum(1,1)
Service.sum(pey,1,1)  ##클래스명을 통해 객체를 접근할때는 self값을 넣는다
pey.func()
