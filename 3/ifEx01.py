##if문

num =5

if num>5:
    print('num:', num)
    print('num이 5보다 크다')
elif num==5:
    print('num이 5와 같다')
else:  
    print('num이 5보다 작다')
    

    
print('실행종료')

##pass 처리
if num>5:
    pass   ## pass는 아무것도 실행하지 않는다
elif num==5:
    print('num이 5와 같다')
else:  
    print('num이 5보다 작다')
    

##in  처리

fruit=['apple','bnanna']
if 'apple' in fruit:
    print('apple이 있어요')
else:
    print('apple이 없어요')
    
