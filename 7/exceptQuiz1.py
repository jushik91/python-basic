import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

##문제 : 숫자지만 문자처리된것에 대해서 출력되도록 함
##예외처리를 이용해서 코딩하시오

list_value=['100','good','5','250','hi','500']
list_temp=['100','5','250']

list_number=[]

for data in list_value:
    try:
        int(data)
        list_number.append(data)
    except:
        pass    

print('list_value에서 숫자만 출력',list_number)







#print('list_value에서 숫자만 출력',list_number)
