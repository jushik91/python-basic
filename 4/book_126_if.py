##coffee = 3
##money = 300
##while money:
##    print('돈을 받았으니 커피를 줍니다')
##    coffee = coffee-1
##    print('남은 커픠의 양은 %d개입니다. '%coffee)
##    if not coffee:
##        print('커피가 다 떨어졌스니다. 판매를 중지합니다')
##        break
##print('실행완료')
##


coffee = 3
while True:
    money=int(input('돈을 넣어주세요'))
    if money ==300:
        print('커피를 줍니다.')
        coffee = coffee -1        
    elif money >300:
        print('거스름돈 %d를 주고 줍니다.'%(money -300))
        coffee = coffee-1
    else:
        print('돈을 다시 돌려주고 커리를 주지 않았습니다..')
        print('남은 커피의 양은 %d입니다'%coffee)
    if not coffee:
        print('커피라 다 떨러졌습니다. 판내중지')
        break
    
print('실행완료')

