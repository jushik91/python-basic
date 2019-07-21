##전역변수
value =10

def show():

    print('run show()')

    print('__name__:',__name__) ##자기파일을 자기가 실행하면 main으로 나옴
                                ## 다른 파일이 import하면서 실행시키면 import파일명이 나옴
                                ##__name__은 파이선은 내장변수


class Increment:
    def printValue(self):
        self.num=100 ##인스턴스변수
        print('num:',self.num)

if __name__=='__main__':  ##자기파일에서 호출할때만 main실행함
    show()
