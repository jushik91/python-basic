print(help(print))

print( 'one','two')
print('one','two', sep=',', end=' ')
print('End')

print('일','이','삼')
#구분자 sep
print('일','이','삼', sep='/')
#구분자 : end
print('일','이','삼', end='END')
print('끝~')

#퀴즈
##출력형태 : 연락처는 010-1111-1111입니다.
print('연락처는' ,end=' ')
print('010','1111','1111', sep='-', end='' )
print('입니다.')


