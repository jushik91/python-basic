##구구단 파일에 1에서 100까지 추가

#with문 : close함수가 자동으로 호출 ->close함수 생략
with open('D:\\pythonProject\\project\\day20190504\\gugu.txt','a') as f:
    for i in range(1,101):
        f.write('{:<3}'.format(i))
        if i%10 ==0:
            f.write('\n')

#    print(f.read())
