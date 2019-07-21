class Calculator:

    number =10  ##클래스 변수

    def __init__(self):
        self.result=0 ##인스턴스 변수

    def adder(self,num):
        self.result +=num
        return self.result

##객체(인스텐스) 생성

cal1= Calculator()
cal2= Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))


print(Calculator.number)  ##클래스변수
