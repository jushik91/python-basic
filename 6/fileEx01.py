##쓰기
#1. Open함수

##file =open('D:\pythonProject\project\day20190504\new.txt','w')  ##경로만 복사하면 에러난다. ctrl+shift+c
##file =open('D:\\pythonProject\\project\\day20190504\\new.txt','w') ##경로복사후 \를 한번 더 넣어준다
file =open('D:\\pythonProject\\project\\day20190504\\new.txt','a') ##a는 기존파일에 추가 기록 한다
##file =open('D:/pythonProject/project/day20190504/new.txt','w') ##경로복사후 /로 변경해도 된다


#2. write함수

file.write('\n1234~~~')
file.write('\nfgfgfg^^^^')

#3.close함수

file.close()

print('successs~~!!!')
