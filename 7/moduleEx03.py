
##방법1
# from testModule import value ##변수/함수/클래스 각자 정의 필요
# from testModule import show
# from testModule import Increment

##방법2
#from testModule import value, show, Increment

##방법3
from testModule import *
#import testModule as tm  ##변수명이 같은 경우에 유용함
#import testModule



print(value)

show()

i = Increment()
i.printValue()
