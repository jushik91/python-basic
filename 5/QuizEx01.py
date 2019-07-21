
##문제 1 four_rules(7,2)

def four_rules(i,j):
    print('{} + {} = {}'.format(i,j,i+j))
    print('{} - {} = {}'.format(i,j,i-j))
    print('{} * {} = {}'.format(i,j,i*j))
    print('{} / {} = {}'.format(i,j,i/j))


four_rules(7,2)

##문제2
def star_count(i):
    print('*'*i)
star_count(7)

##문제 3

def accumulator(a,b):
    sum=0
    (max,min)= (a,b) if(a>b) else (b,a)
    for n in range(min, max+1):
        sum +=n

    print('sum=',sum)



accumulator(1,10)
accumulator(9,1)
