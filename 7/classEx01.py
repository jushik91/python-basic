##클래스 상속 예졔/상속 예부 내장함수, 오버라이딩 예제


class Mother:
    money = 1000000 ##class변수

    def buy(self):
        Mother.money -= 200000
    def balance(self):
        print('balance:',Mother.money)

class Son(Mother):
    pass
    def buy(self,money):    ##메서드 오버라이딩 : 자식이 부모의 함수를 재정의해서 씀
        Mother.money -=money



s=Son()
s.buy(600000)
s.balance()

m=Mother()
m.buy()
m.balance()

##파이썬 기본 내장함수

print(issubclass(Son,Mother)) ##상속관계인지 확인,앞쪽이 자식,뒤쪽이 부모
print(issubclass(Mother,Son)) ##상속관계인지 확인

print(isinstance(s,Son))  ## s가 Son의 instance 인지
print(isinstance(s,Mother))
