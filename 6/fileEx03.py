

#1. Open함수

#2. readlines함수

#3. close함수


#with문 : close함수가 자동으로 호출 ->close함수 생략
with open('D:\\pythonProject\\project\\day20190504\\gugu.txt','r') as f:
    for line in f:
        print(line,end='')
#    print(f.read())
