##읽기

##1.Open함수
f=open('D:\\pythonProject\\project\\day20190504\\gugu.txt','r')

##2-1.read 함수
text = f.readline()
print(text, end='')
#print(text)


##2-2.read 함수
# while True:
#     text=f.readline()
#     if not text:
#         break
#     print(text, end='')


## readlines함수 //리스트형태로 읽어옴
#text = f.readlines()
#print(text[3])
#print(text)

##readlines  list로 읽어옴
 # text = f.readlines()
 # for i in text:
 #     print(i, end='')
 #     print(text)

## read : 문자열형태로 저장 str
# text= f.read()
# print(type(text))
# print(text[:50])




##3.close함수
f.close()
