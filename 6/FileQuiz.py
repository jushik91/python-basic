
#1. Open함수

file=open('D:\\pythonProject\\project\\day20190504\\gugu.txt', 'w')

for i in range(2,10):
    for j in range(1,10):
        ##file.write('{} * {} = {}\n'.format(i,j,i*j))
        file.write('%d * %d = %d\n'%(i,j,i*j))
    file.write('\n')


file.close()
