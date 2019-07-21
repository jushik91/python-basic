
for num in [2,4,6,8]:
    print(num)

for i in range(1,3):
    print('Outer Loop:{}번째 실행'.format(i))
    for j in range(1,4):
        print('\t Inner loop : {}번째 실행:'.format(j))
    
##구구단
for i in range(2,10):    
    for j in range(1,10):
        print('{} * {} = {}'.format(i,j,i*j))
    print('\n')

print('*'*30)
##구구단 : 짝수단
for i in range(2,10,2):    
    for j in range(1,10):
        print('{} * {} = {}'.format(i,j,i*j))
    print('\n')

##구구단 : 짝수단중에서 2단은 2개, 4단은 4개    
idx=1
for i in range(2,10,2):    
    for j in range(1,i+1):
        print('{} * {} = {}'.format(i,j,i*j))
    print('\n')
