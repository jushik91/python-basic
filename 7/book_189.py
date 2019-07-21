class FourCal:

    def setdata(self,first,second):
        self.first=first
        self.second = second

    def sum(self):
        result=self.first + self.second
        return result

    def mul(self):
        result=self.first * self.second
        return result

    def sub(self):
        result=self.first - self.second
        return result

    def div(self):
        result=self.first/self.second
        return result




##객체(인스턴스) 생성
a=FourCal()

a.setdata(4,2) #방법 1
#FourCal.setdata(a,4,2)  ##방법2
#FourCal.setdata(FourCal(),4,2)  ##방법2

print('sum:',a.sum())
print('mul:',a.mul())
print('sub:',a.sub())
print('div:',a.div())

print(type(a))
