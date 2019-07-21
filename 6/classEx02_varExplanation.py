class Person():
    ##생성자 : 객체 생성시 자동으로 호출하는 것은 생성자
    ##생성자 용도 : 1) 객체생성하면서 인스턴드 변수의 값을 자동 초기화
    ##             2) 객체 생성시 자동으로 함수를 수행하고 싶을 때ㅔ
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.test()
        ##print('run init')

    def setName(self,name):
        nick = 'gong' ##지역변수
        self.name=name

    def setAge(self,age):
        self.age = age

    def info(self):
        print('name:{}, age:{}'.format(self.name,self.age))

    def test(self):
        print('test~~~!!!')

p = Person('Jang', 33)

#p.setName('kim')
#p.setAge(25)
p.info()
