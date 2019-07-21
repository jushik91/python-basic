##class 정의
##   : class는 자료형

##class 함수는 멤버함수
##class 내의 변수는 멤버변수라고 하는데 멤버함수에서 가져다
##멤버변수는 별도 선언언하고 미리 선언하고 self.+변수로 사용한다.
##지역변수
##로켈변수
##멤버변수 : 인스턴세변수(인스턴스마다 다로 만들어짐)
            ##함수 안에서만 만들수 있다.
##clas변수 : class로 생성된 객체가 공유해서 사용
            ##  student로 관리되는 영역에 nick이 따로 만들어짐
            ## 클래스명으로 접근



class Student():  ##클래스는 대문자로 보통 한다.

    nick = 'google' ##class변수, 클래스 바로 아래에다 만들어야 한다

    def study(self):
        print('study~~~!!!!')
        print('name:',self.name)
        print('nick:', Student.nick)

    def setName(self,name):
        self.name=name  ## name은 지역변수, self.name은 멤버변수
        print('nick:', Student.nick)

print(Student.nick)  ## class 변수는 객체를 안만들어도 바로 사용할 수 있다
#print(self.name)  ## 멤버 변수는 clas 없이 사용 불가

s = Student()
s1 = Student()

s.setName('Kim')
s1.setName('Hong')

s.study()
s1.study()
