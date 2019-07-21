import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class HousePark:
    lastname="박"

    # def __init__(self,name):
    #     self.fullname=HousePark.lastname + name

    def setname(self,name):
        ##self.fullname=self.lastname+name ##lastname이 클래스변수인데 self를 붙여도 되는것인가? 가능함
        self.fullname=HousePark.lastname + name ## 더 맞는 형태

    def printInfo(self):
        print('fullname:', self.fullname)

    def travel(self,where):
        print('%s,%s여행을 가다'%(self.fullname,where))

class HouseKim(HousePark):
    lastname='김'


pey=HousePark()
pes=HousePark()

print(pey.lastname)
print(pes.lastname)

pey.setname('응용')
pey.printInfo()

pey.travel('부산')
