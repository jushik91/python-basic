import sys

args = sys.argv  ## 입력된 것을 저장한다.
##args = sys.argv[1:]  ## 파일명 출력 안함

print(type(args))

for i in args:
    #print(i)
    print(i.upper(), end = ' ')
