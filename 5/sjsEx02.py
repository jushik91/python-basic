##백
import sys
n=int(sys.stdin.readline())
 
for _ in range(n):
    plist = list(sys.stdin.readline())    # 입력->리스트
 
    while plist != []:
        if plist[0] == ')':             # 시작이 ): NO
            print('NO')
            break
        else:
            if ')' in plist:
                plist.remove('(')
                plist.remove(')')       # 괄호 쌍 제거
            else:                       # 괄호 쌍X: NO
                print('NO')
                break
 
    if plist == []:
        print('YES')

 
 
 
