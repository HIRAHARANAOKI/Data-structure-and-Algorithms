# デッキをシャッフルするshuffleDeckメソッドを作成して、シャッフル前のデッキとシャッフル後のデッキをコンソールに表示してみましょう。
class Card:
    def __init__(self, value, suit, intValue):
        self.value = value
        self.suit = suit
        self.intValue = intValue

    def getCardString(self):
        return self.suit + self.value + "(" + str(self.intValue) + ")"


class Deck:
    def __init__(self):
        self.deck = self.generateDeck()

    @staticmethod
    def generateDeck():
        newDeck = []
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["♣", "♦", "♥", "♠"]

        for suit in suits:
            for i, value in enumerate(values):
                newDeck.append(Card(value, suit, i + 1))

        return newDeck

    def printDeck(self):
        print("Displaying cards...")
        for card in self.deck:
            print(card.getCardString())

    # ここから記述してください。
    def shuffleDeck(self):
        sizeDeck = len(self.)


card1 = Deck()
card1.printDeck()

# シャッフル後のデッキを出力してください。