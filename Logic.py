import Deck

#Logic Inherits Deck ideally it should have access to its methods as well


class Logic(Deck):

    def testDeck(self):
        Deck.build_deck()
        for card in Deck:
            print(card)

test = Logic

test.testDeck()