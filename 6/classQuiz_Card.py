##Card 클래스를 정의하시오.
##클래스를 계속 Add해 가기

class Card():



    def __init__(self, num,kind):
        self.num=num
        self.kind=kind

    def print_card(self):
        print('card number:{}, card kind:{}'.format(self.num,self.kind))

c1=Card(4,'spade')
c2=Card(1,'King')
c3=Card(2,'diamond')

c3.print_card()
