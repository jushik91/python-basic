class Bird:
    def fly(self):
        ##print('run fly method')
        raise NotImplementedError ### 함수를 자식 클래스에서 반드시 재정의해라

class Eagle(Bird):
    def fly(self):
        print('overiding method')

e=Eagle()
e.fly()
