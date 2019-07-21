def sum_many(*args):  ## args는 이름을 바꿔도 된다, args는 튜블값으로 값을 받는다
    print(type(args))
    sum=0
    for i in args:
        sum = sum + i
    return sum

result=sum_many(2,3,4)
print(result)
