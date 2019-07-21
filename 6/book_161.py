path='D:\\pythonProject\\project\\day20190504\\newfile.txt'
f=open(path, 'w')

for i in range(1,11):
    data='%d번째 줄입니다.\n'%i
    f.write(data)

f.close()
