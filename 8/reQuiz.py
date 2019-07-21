import re

data='''
0001 park 010-1111-1111
0002 kim 010-2222-2222
'''

#전화번호만 추출

c=re.compile('\d{3}-\d{4}-\d{4}')
d=c.findall(data)
print(d)
