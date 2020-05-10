class Card:
    ACE, JACK, QUEEN, KING = 'A', 'J', 'Q', 'K'
    FACES = (ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING)
    SUITS = tuple(map(chr, (9824, 9827, 9829, 9830)))
    SPADE, CLUB, HEART, DIAMOND = SUITS

    def __init__(self, suit, face):
        self._suit = suit
        self._face = face

    def __int__(self):
        if self._face in {Card.JACK, Card.QUEEN, Card.KING}:
            return 10
        return 1 if self._face == Card.ACE else self._face

    def __str__(self):
        return self._suit + str(self._face)

    def __repr__(self):
        return __class__.__name__ + repr((self._suit, self._face))

class Deck:
    def __init__(self):
        self._deck = [Card(suit, face) for suit in Card.SUITS \
                for face in Card.FACES]

    def shuffle(self):
        import random
        random.shuffle(self._deck)

    def __iter__(self):
        return iter(self._deck)

def BlackJack():
    D = Deck()
    D.shuffle()
    total = 0
    it = iter(D)
    while True:
        c = next(it)
        total += int(c)
        print(f'your card: {c}, total = {total}.', end = '')
        if total > 21:
            print(f'You lose! total = {total}')
            break
        if total == 21:
            print('You win! total = 21')
            break
        ans = input('More cards? [y/n] ')
        if ans not in {'Y', 'y'}:
            c = next(it)
            print(f'Next card is {c}. You' + (' win' if total + int(c) > 21 else ' lose'))
            break
