##[방법1]
##import 모듈명

import random
#
# print('random:', random.random()) ##random파일의 random()함수를 호출함


##[방법2]
##from 모듈명 import 함수명/변수명/클래스명으로

# from random import random  ##앞쪽 파일, 뒤쪽 함수명
# print('random:', random())  ##앞에 파일명을 제거한다


##[방법3]
##import 파일명 as 별명
# import random as r
# print('random:', r.random())


######################### random함수의 종류#####
print('random.uniform(1,10):', random.uniform(1,10)) ##random 범위제공
print('random.randrange(10):', random.randrange(10)) ## 정수형태 (0에서부터 9까지중 고른다)
print('random.randrange(1,100):', random.randrange(1,100)) ##정수형태 범위(1~99까지 정수)
print('random.choice[2,4,6,8]:', random.choice([2,4,6,8])) ##리스트값중 random으로 추출
