import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class HousePark:
    lastname="박"

    def __init__(self,name):
        self.fullname=self.lastname + name

    def setname(self,name):
        self.fullname=self.lastname+name ##lastname이 클래스변수인데 self를 붙여도 되는것인가? 가능함
    ##    self.fullname=HousePark.lastname + name ## 더 맞는 형태

    def printInfo(self):
        print('fullname:', self.fullname)

    def travel(self,where):
        print('%s,%s여행을 가다'%(self.fullname,where))

class HouseKim(HousePark):
    lastname="김"

    def travel(self,where,day):
        print('%s,%s여행을 %d일 가네'%(self.fullname,where,day))


pey=HousePark('보검')
pey.travel('부산')

juliet = HouseKim('줄리엣')
juliet.travel('독도',10)   ##김줄리엣이라고 인쇄되어야 함 check 필요
