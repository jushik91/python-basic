class Student:
    mem_num = 1

    def __init__(self,name):
        self.name = name

    def greeting(self):
        print('Hello, my name is', self.name)
        print('mem_num', self.mem_num)

print(Student.mem_num)
