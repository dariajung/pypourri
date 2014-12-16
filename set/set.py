# number (one, two, or three);
# symbol (diamond, squiggle, oval);
# shading (solid, striped, or open);
# and color (red, green, or purple)

import random


class Game(object):
    def __init__(self):
        self.cards = self.generate_cards()
        self.cards_in_play = self.set_up()

    # look at iter tools
    def generate_cards(self):
        number = ["one", "two", "three"]
        symbol = ["diamond", "squiggle", "oval"]
        shading = ["solid", "striped", "open"]
        color = ["red", "green", "purple"]

        cards = []

        for num in number:
            for sym in symbol:
                for shade in shading:
                    for c in color:
                        card = (num, sym, shade, c)
                        cards.append(card)

        random.shuffle(cards)
        return cards

    # going to set up the initial board
    def set_up(self):

        cards_in_play = []

        for x in range(0, 16):
            cards_in_play.append(self.cards.pop())

        return cards_in_play


if __name__ == "__main__":
    game = Game()
    assert len(game.cards_in_play) == 16
    print game.cards_in_play
    assert len(game.cards) == (81 - 16)

    print "tests passed"
