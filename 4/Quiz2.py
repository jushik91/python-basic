##사용자에게서  5개의 정수를 받음
    
idx=1
data=[]
sum=0

while idx<6 :    
    num=int(input('{}번째:<정수입력>:'.format(idx)))
    data.append(num)
    sum = sum+num
    idx +=1

print('누적합:',sum)   
print('입력된값 모두 출력:',data)            
    



              
