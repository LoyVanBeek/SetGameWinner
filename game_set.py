"""
% the Set-game.
% In Set, 12 cards are placed on the table.
% Each card has some object(s) depicted. A card has 4 'parameters':
%  - number
%  - shape
%  - filling
%  - colour
%
%  The objective is to find sets (|set| = 3) of cards that have all of
%  these properties the same, or, per property all different. See the
%  web if needed: https://secure.wikimedia.org/wikipedia/en/wiki/Set_(game)
%  and http://tao-game.dimension17.com/
%
%: card(Colour, Shape, Fill, Count).
% number (one, two, or three);
% symbol (diamond, squiggle, oval);
% shading (solid, striped, or open);
% and color (red, green, or purple)
"""
import itertools
import random

numbers     = (1,2,3)
shapes      = ("diamond",   "squiggle", "oval")
fills     = ("solid",     "striped",  "open")
colors      = ("red",       "green",    "purple")


class Card(object):
    def __init__(self, color, shape, fill, number):
        assert color in colors
        assert shape in shapes
        assert fill in fills
        assert number in numbers
        
        self.color = color
        self.shape = shape
        self.fill = fill
        self.number = number

    def __repr__(self):
        return "Card(%s, %s, %s, %i)"%(self.color, self.shape, self.fill, self.number)

    def __getitem__(self, index):
        return self.__dict__[index]

def color_same(cards, n=3):
    assert len(cards) == n
    return (cards[0].color == cards[1].color == cards[2].color)

def attr_same(cards, attr):
    first = cards[0][attr]
    same = all((card[attr] == first for card in cards))
    return same

def attr_diff(cards, attr):
    values = [card[attr] for card in cards]
    if sorted(list(values)) == sorted(list(set(values))):
        return True
    else:
        return False

def findsets(cards, n=3):
    """cards is a list of Card-objects.
For each possible pair of n cards, verify if it is a set"""
    attributes = ("color", "shape", "fill", "number")
    sets = set()
    for triple in itertools.combinations(cards, n):
        #if for all attributes, the attribute is either all the same of totally different:
        if all((attr_diff(triple, attribute) or attr_same(triple, attribute) for attribute in attributes)): 
            sets.add(tuple(sorted(triple))) #don't add multiple sets with the same card, only with different orders. 
    return sets

def generate_all_cards():
    """Generates all possible combinations of properties"""
    for color in colors:
        for fill in fills:
            for shape in shapes:
                for num in numbers:
                    yield Card(color, shape, fill, num)


all_cards = list(generate_all_cards())
table = random.sample(all_cards, 12)

c1 = Card("green", "squiggle", "solid", 1)
c2 = Card("green", "oval", "open", 2)
c3 = Card("green", "diamond", "striped", 3)
c4 = Card("green", "diamond", "solid", 3)
allcards = [c1, c2, c3, c4]
set1 = [c1, c2, c3]
noset = [c1, c2, c4]

def brute():
    sets = findsets(all_cards)#findsets(random.sample(all_cards, 15))#findsets(set1)
    for s in sets:
        for card in s:
            print card
        print "-------"
    return sets

if __name__ == "__main__":
##    sets = brute()
    k1 = Card("purple", "squiggle", "solid", 1)
    k2 = Card("purple", "squiggle", "striped", 1)
    k3 = Card("purple", "oval", "open", 1)
    k4 = Card("green", "squiggle", "open", 1)
    k5 = Card("purple", "squiggle", "open", 3)
    k6 = Card("green", "diamond", "solid", 2)
    k7 = Card("purple", "diamond", "solid", 3)
    k8 = Card("red", "oval", "open", 1)
    k9 = Card("red", "oval", "open", 2)
    k10 = Card("red", "diamond", "open", 3)
    k11 = Card("green", "oval", "open", 2)
    k12 = Card("purple", "diamond", "solid", 1)
    cards = [k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12]
    findsets(cards)
