#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author : Matthieu Keller <keller.mdpa@gmail.com>

""" BE note
"""
import random


class Card(object):
    """ Dictionnaire couleur->no
    """
    color_code = {'pique' : 0, 'coeur' : 1, 'trefle' : 2, 'carreau' : 3}
    value_code = {"as" :12, "roi": 11, "dame": 10, "valet":9, "dix": 8,\
        "neuf": 7, "huit":6, "sept":5, "six":4, "cinq":3, "quatre":2,\
        "trois": 1, "deux": 0}
    def __init__(self, value, color):
        """ Init a card with his value and his color
        """
        self.color = Card.color_code[color]
        self.value = Card.value_code[value]

    def __hash__(self):
        """ overload the hash operator in order to associate a unique hash to a card
        """
        return (self.value)+13*(self.color)

    def __eq__(self, card):
        """ overload equal operator
        """
        if self.color == card.color and self.value == card.value:
            return True
        else:
            return False

    def __gt__ (self, card):
        """ overload greater than operator
            """
        if self.value > card.value:
            return True
        else:
            return False

    def __lt__ (self,card):
        """ overload lesser than operator
        """
        if self.value < card.value:
            return True
        else:
            return False

    def __str__ (self):
        """ overload toString operator
        """
        return "color :"+str(self.color) + "value"+str(self.value)

class Poker(object):
    def gen_fifths(self):
        """ generate fifths list in order to test isQuinte
        """
        fifth = [-1]*9
        lst=sorted(Card.value_code.items(), lambda x,y: (x[1]-y[1]))
        for i in range(9):
            fifth[i] = set([lst[i+j][0] for j in range(5)])
        return fifth
    def gen_game(self):
        """ generate all cards of a poker game (52 Cards)
        """
        game = set()
        for color in Card.color_code.keys():
            for value in Card.value_code.keys():
                game.add(Card(value, color))
        return game
    def gen_color(self):
        """ generate color list in order to test isColor
        """
        color = [-1]*4
        for couleur in Card.color_code.keys():
            oneColor = set()
            for value in Card.value_code.keys():
               oneColor.add(Card(value, couleur))
            color[Card.color_code[couleur]] = oneColor
        return color
    def gen_value(self):
        """ generate value list in order to test isSquare
        """
        value = [-1]*13
        for valeur in Card.value_code.keys():
            oneValue = set()
            for color in Card.color_code.keys():
                oneValue.add(Card(valeur, color))
            value[Card.value_code[valeur]] = oneValue
        return value

    def random_set(self):
        """ generate a random hand
        """
        random_set = random.sample(self.gen_game(), 5)
        deck = set()
        for card in random_set:
            deck.add(card)
        return deck

    def isColor (self, deck):
        """ test if the deck is a Flush
        """
        colors = self.gen_color()
        for color in colors:
            if len(deck.intersection(color)) == 5:
                return True
        return False

    def isQuinte(self, deck):
        """ test if the deck is a Straight
        """
        code_table = {12: "as", 11 : "roi", 10 : "dame", 9 : "valet", 8 : "dix", 7 : "neuf", 6 : "huit", 5 : "sept", 4 : "six", 3 : "cinq", 2 : "quatre", 1 : "trois", 0 :"deux"}
        fifths = self.gen_fifths()
        plop = set()
        for card in deck:
            nb = hash(card) - 13*card.color
            plop.add(code_table[nb])
        for fifth in fifths:
            if len(plop.intersection(fifth)) == 5:
                return True
        return False

    def isQuinteFlush(self, deck):
        """ test if the deck is a Straight Flush eg isQuinte and isColor
        """
        return self.isQuinte(deck) and self.isColor(deck)

    def isSquare (self, deck):
        """ test if the deck is a Four of a Kind
        """
        values = self.gen_value()
        tmp = set()
        for value in values:
            if len(deck.intersection(value)) == 4:
                return True
        return False

    def isThree (self, deck):
        """ test if the deck is a Three of a Kind
        """
        values = self.gen_value()
        for value in values:
            if len(deck.intersection(value))==3:
                return True
        return False

    def isOnePair (self, deck):
        """ test if the deck is a One Pair
        """
        values = self.gen_value()
        for value in values:
            if len(deck.intersection(value)) == 2:
                return True
        return False

    def isTwoPair (self, deck):
        """ test if the deck is a Two Pair
        """
        c = 0
        values = self.gen_value()
        for value in values:
            if len(deck.intersection(value)) == 2:
                c+=1
        return c==2

    def isFull (self, deck):
        """ test if the decj is a Full House
        """
        return self.isOnePair(deck) and self.isThree(deck)

    def isCombinaison (self, deck):
        """ test if the deck is a combinaison
        """
        if self.isColor(deck) or self.isQuinte(deck) or self.isSquare(deck) or self.isOnePair(deck) or self.isThree(deck):
            return True
        else:
            return False

    def wichHand(self, deck):
        """ return :
            8 for a Straight Flush (Quinte Flush eg Color and Quinte)
            7 for a Four of Kind (Square)
            6 for Full House
            5 for a Flush (Color)
            4 for a Straight (Quinte)
            3 for a Three of Kind
            2 for a Two Pair
            1 for a Pair
            else 0
        """
        if self.isQuinteFlush(deck):
            return 8
        if self.isSquare(deck):
            return 7
        if self.isFull(deck):
            return 6
        if self.isColor(deck):
            return 5
        if self.isQuinte(deck):
            return 4
        if self.isThree(deck):
            return 3
        if self.isTwoPair(deck):
            return 2
        if self.isOnePair(deck):
            return 1
        return 0

    def isBetterHand(self, deck1, deck2):
        """ return True is deck1 is a better hand than deck2
        """
        return self.wichHand(deck1) > self.wichHand(deck2)

    def isWorseHand(self, deck1, deck2):
        """ return True is deck1 is a worse hand than deck2
        """
        return self.wichHand(deck1) < self.wichHand(deck2)

    def isSameHand(self, deck1, deck2):
        """ return True is deck1 is the same hand than deck2
            for now a pair is equal to a pair
            in realty a pair of as is better than a pair of 8
        """
        return self.wichHand(deck1) == self.wichHand(deck2)



if __name__ == "__main__":
    i = 0
    cont = False
    while (not cont):
       i+=1
       game = Poker()
       deck = game.random_set()
       cont = game.isCombinaison(deck)
    print i
