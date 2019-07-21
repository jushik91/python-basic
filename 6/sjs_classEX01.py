class Student():

    nick='Google'
    employee='Jushik'

    def __init__(self,name,age):
        self.name=name
        print('init:self.name', self.name)

    def study(self):
        print("I am practicing ")
        print('self.mother-->',self.mother)

    def setname(self,name):
        self.name=name
        self.father=name
        self.mother=name
        print('nick:',Student.nick)
        print('nick:',name)
        print('father:',self.father)

print(Student.nick)
print(Student.employee)
s=Student('song',25)
##s1=Student()

s.setname('song')
s.study()
