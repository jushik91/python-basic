##treeHit=0
##while treeHit <10:
##    treeHit = treeHit +1
##    print("나무를 %d번 찍었습니다." %treeHit)
##    if treeHit ==10:
##        print('나무를 넘어갑니다')
##        


prompt ="""
1.Add
2.Del
3.List
4.Quit

Enter number:"""


number =0
while number !=4:  # 
    print(prompt,end ='')
    number = int(input())
    if number==1:
        print('1.Add')
    elif number==2:
        print('2.Del')
    elif number==3:
        print('3.List')
    else:
        print('4.Quit')

print('-------------')
print('실행완료')
print(prompt)

##elif number ==2
##        print('2.Del')
##    elif number ==3
##        print('3.List')   
