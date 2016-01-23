import Deck

class Card():
    # each card has a number type and the seperator of
    def __init__(self, number, type):
        self.num = number
        self.type = type
        assert isinstance(self.type, Card)
        return str(self.num + " of " + self.type)

    cardType = ["Hearts", "Spades", "Diamonds", "Clubs"]
    cardValue = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
