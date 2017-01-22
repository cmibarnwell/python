import random
def draw_card():
    suit_num=random.randrange(1,4)
    if suit_num==1:
        suit="Hearts"
    elif suit_num==2:
        suit="Diamonds"
    elif suit_num==3:
        suit="Spades"
    else:
        suit="Clubs"

    card_num=random.randrange(2,14)
    if card_num==11:
        card= "Jack"
    elif card_num==12:
        card= "Queen"
    elif card_num==13:
        card= "King"
    elif card_num==14:
        card= "Ace"
    else:
        card=card_num
    print("Your card is a(n)",card,"of",suit)

draw_card()
