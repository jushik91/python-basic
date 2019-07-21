a=[1,2,3]  ##리스트
b=(1,2,3)  ##튜플

#딕셔너리
# -하나의 데이타가 쌍으로 관리
# - 키와 값이 하느이 데이타
# - 저장 순서를 유지하지 않아요

dic={'name':'kim','phone':'010-1111-1111'}

print(dic['name'])
print(dic['phone'])

dic['address']='gangnam'
print(dic)

##del dic['phone']
##print(dic)

dic['age']=25  ## 키값이 없을때는 추가한다
print(dic)

dic['name']='park'  ## 키값이 있을때는 변경된다
print(dic)

key=dic.keys()  ## keys() 는 키만 뽑아온다
key=list(dic.keys())  ## 자료형을 list로 변경한다
print(key)
print(type(key))

print('key[0]:',key[0])  ##dictionary는 인덱스 형태 사용 불가


##print(dic.values())  ##values()는 값만 뽑아온다.

it= list(dic.items())  ## 키와 값을 쌍으로 뽑아온다.
print('it의 자료형:',type(it))
print(it)
print(it[0])
print(type(it[0]))

print(dic.get('name'))
print(dic.get('addr','DEFULAT값'))   ## print(dic.get('addr','default'))
print(dic['address'])  

print('name' in dic)     ## in은 찾고자 하는 키값을 넣는다
print('addr' in dic)

dic.clear()   ## dictionary요소를 모두 지운다
print(dic)

