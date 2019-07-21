value=[2,4,6,8,'hi~~',[1,3,5],2.5]
print(type(value)) #자료형 List
print(value)
print('1번째데이타:',value[0])
print('4번째데이타:',value[3])
print('2번째,3번째데이타:',value[1:3])
print('5번째데이타:',value[4])
print('마지막데이타:',value[-1])

print('마지막데이타 자료형:',type(value[-1])) #자료형 Float

print('리스트요소 중 3  출력:',value[-2][1])
print('문자열 요소   출력:',value[4])
print('문자열 요소 중 i만  출력:',value[4][1])      

mix_value=[1,2,3, 'one','two','three']
value = [1,2,3,['one','two','three']]

##QUIZ
#mix_value에서 one, two 출력
print(mix_value[3:5])
print(type(mix_value[3:5]))
## value에서 one, two 출력
print(value[-1][0:2])














