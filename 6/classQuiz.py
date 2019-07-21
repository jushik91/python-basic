##생성자를 통해서 강이지 이름을 입력받아 저저장
#showName을 통해서 강아지 이름을 출력

class Dog():

    def __init__(self,name):
        self.name=name

    def showName(self):
        print('Dog name is {}'.format(self.name))

d = Dog('Scuby')
d.showName()
