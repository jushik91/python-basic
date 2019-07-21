##라인복사
##

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


path='D:\\pythonProject\\project\\day20190504\\newfile.txt'
f=open(path, 'r')

# line = f.readline()
# print(line)
# f.close()

while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()
