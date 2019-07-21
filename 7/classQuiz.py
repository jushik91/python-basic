class Card:
    card_info={} ##class 변수, 딕션너리선언!!
    def __init__(self,number,kind):
        Card.card_info[number]=kind

    def print_card(self):
        for key,value in Card.card_info.items():
            print('card number:{},card kind:{}'.format(key,value))

##객체(인스턴스) 생성
c1=Card(4,'spade')
c2=Card(1,'king')
c3=Card(2,'diamind')

c1.print_card()
