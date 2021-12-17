def Card_box():
    card_suit = ('diamonds', 'clubs', 'hearts', 'spades')
    card_Big = ('A','K','Q','J')+tuple(range(2,11))
    for j in card_suit:
        for i in range(len(card_Big)):
            if i<4:
                yield card_Big[i]+'-'+j
            else:
                yield str(card_Big[i])+'-'+j



Card = Card_box()
try:
    for i in range(60):
        print(next(Card))
except StopIteration:
    print('StopIteration')
