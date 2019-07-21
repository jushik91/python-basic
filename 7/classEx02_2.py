import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Animal:  ##일반적으로 부모 클래스는 간단하게, 추상적으로.
    def __init__(self,name):  ##첫번째 매개변수는 꼭 있어야 하는데, self라오 안써도 됨
        self.name=name

    def print_name(self):
        print('이름은 {}입니다.'.format(self.name))


class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)  ##자바는 super라고만 씀
        print('Dog__init__')

        self.sound()

    def sound(self):
        print('{}가 멍멍 짖어요'.format(self.name))

    def testprint(self):
        print('run testPrint()')


class Cat(Animal):
    def sound(self):
        print('{}가 야옹소리를내요'.format(self.name))


##[방법1]객체생성없이 클래스 함수를 호출
#Dog.testprint(Dog('happy'))  ##self만 있을때는 매개변수를 넣을필요가 없는데,,
                             ## class명을 통해 함수를 바로 호출시는 self라도 매개변수 추가-직접 주소입력

##[방법2] 객체 생성 후 클래스 함수를 호출
  d= Dog('happy')
  Dog.testprint(d)


##[방법3] 객체를 생성후 객체함수를 호출
# d=Dog('happy')
# d.print_name() #
#d.sound()

# c=Cat('world')
# c.print_name()
# c.sound()
