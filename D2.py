import Card

''' this is the second version of the Deck class and it will inherit Card so that it may store it's values, but all
the methods will determine its values. this is just a test class at this point. Also working on inheritance '''


class D2(Card):
    def __init__(self,DeckOCards):
        # call a method to build an set this value equal to the built list of cards. May need to copy the list to this
        # property once it is built

        # deck of cards property as a list
        self.deck = type(DeckOCards, list)

    def build_test(self):
        c = Card
        d = D2
        DeckOCards = []
        for number in Card.Card.cardValue:
            for suit in Card.Card.cardType:
                c.Card.num = number
                c.Card.type = suit
                Card(number,suit)
                DeckOCards.append(Card)
        return DeckOCards

newDeck = D2

newDeck.build_test()

for Card in newDeck.DeckOCards:
    print(Card)




