#사용자가 입력할 데이타를 파일에 저장하도록 입력하시오


# while True:
#     a=input('기록할데이타 입력:')
#     print(a)

#
path='D:\\pythonProject\\project\\day20190504\\userInputData.txt'
f=open(path, 'a')

while True:
    text=input('기록할데이타 입력:')
    if not text:  //데이타가 하나도 없으면
        break
    f.write(text +'\n')

f.close()
