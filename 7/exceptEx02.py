
n1 = 5
n2 = 0 ##0

result1,result2 = 0, 0

try:
    result1= n1/n2
    result2=n1%n2
except:
    print('exception')
else:
    print('n1/n2:',result1)
    print('n1%n2:',result2)

finally:
    print('exceptioin end!!')

print('success!!')
