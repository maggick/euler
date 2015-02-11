#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


class Card(object):
    """ Dictionnaire couleur->no
    """
    color_code = {'C': 0, 'D': 1, 'S': 2, 'H': 3}
    value_code = {"A": 12, "K": 11, "Q": 10, "J": 9, "T": 8,
                  "9": 7, "8": 6, "7": 5, "6": 4, "5": 3,
                  "4": 2, "3": 1, "2": 0}

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

    def __gt__(self, card):
        """ overload greater than operator
            """
        if self.value > card.value:
            return True
        else:
            return False

    def __lt__(self, card):
        """ overload lesser than operator
        """
        if self.value < card.value:
            return True
        else:
            return False

    def __str__(self):
        """ overload toString operator
        """
        return "color: "+str(self.color) + " value: "+str(self.value)


class Poker(object):
    def gen_fifths(self):
        """ generate fifths list in order to test isQuinte
        """
        fifth = [-1]*9
        lst = sorted(Card.value_code.items(), lambda x, y: (x[1]-y[1]))
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
        """ generate value list """
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

    def isColor(self, deck):
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
        code_table = {12: "A", 11: "K", 10: "Q", 9: "J", 8: "T",
                      7: "9", 6: "8", 5: "7", 4: "6", 3: "5",
                      2: "4", 1: "3", 0: "2"}
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

    def isSquare(self, deck):
        """ test if the deck is a Four of a Kind
        """
        values = self.gen_value()
        for value in values:
            if len(deck.intersection(value)) == 4:
                return True
        return False

    def isThree(self, deck):
        """ test if the deck is a Three of a Kind
        """
        values = self.gen_value()
        for value in values:
            if len(deck.intersection(value)) == 3:
                return True
        return False

    def isOnePair(self, deck):
        """ test if the deck is a One Pair """
        values = self.gen_value()
        for value in values:
            if len(deck.intersection(value)) == 2:
                return True
        return False

    def isTwoPair(self, deck):
        """ test if the deck is a Two Pair """
        c = 0
        values = self.gen_value()
        for value in values:
            if len(deck.intersection(value)) == 2:
                c += 1
        return c == 2

    def isFull(self, deck):
        """ test if the deck is a Full House """
        return self.isOnePair(deck) and self.isThree(deck)

    def isCombinaison(self, deck):
        """ test if the deck is a combination """
        if self.isColor(deck) or self.isQuinte(deck) or self.isSquare(deck)\
                or self.isOnePair(deck) or self.isThree(deck):
            return True
        else:
            return False

    def searchHighCard(self, deck):
        tmp = -1
        for card in deck:
            if card.value > tmp:
                tmp = card.value
        return tmp

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
            else 0 """
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

    def getPairValue(self, deck):
        values = self.gen_value()
        tmp = ''
        for value in values:
            if len(deck.intersection(value)) == 2:
                for v in value:
                    tmp = v
                    break
        return tmp.value

    def getThreeValue(self, deck):
        values = self.gen_value()
        tmp = ''
        for value in values:
            if len(deck.intersection(value)) == 3:
                for v in value:
                    tmp = v
                    break
        return tmp.value

    def getSquareValue(self, deck):
        tmp = 1
        values = self.gen_value()
        for value in values:
            if len(deck.intersection(value)) == 4:
                for v in value:
                    tmp = v
                    break
        return tmp.value

    def isBetterPair(self, deck1, deck2):
        if self.getPairValue(deck1) == self.getPairValue(deck2):
            v = self.getPairValue(deck1)

            # remove pair from deck1
            to_remove = []
            for c in deck1:
                if c.value == v:
                    to_remove.append(c)
            for c in to_remove:
                deck1.remove(c)

            # remove pair from deck2
            to_remove = []
            for c in deck2:
                if c.value == v:
                    to_remove.append(c)
            for c in to_remove:
                deck2.remove(c)

            return self.isBetterHand(deck1, deck2)

        return self.getPairValue(deck1) > self.getPairValue(deck2)

    def isBetterHand(self, deck1, deck2):
        """ return True is deck1 is a better hand than deck2 """
        # is there a better hand than an other ?
        if self.wichHand(deck1) > self.wichHand(deck2):
            return True
        if self.wichHand(deck1) < self.wichHand(deck2):
            return False

        # no clear distinction between the two hands
        if self.wichHand(deck1) != 0 and\
                self.wichHand(deck1) == self.wichHand(deck2):

            if self.isQuinteFlush(deck1):
                if self.searchHighCard(deck1) == self.searchHighCard(deck2):
                    print 'DRAW'
                return self.searchHighCard(deck1) > self.searchHighCard(deck2)
            if self.isSquare(deck1):
                return self.getSquareValue(deck1) > self.getSquareValue(deck2)
            if self.isFull(deck1):
                return self.getThreeValue(deck1) > self.getThreeValue(deck2)
            if self.isColor(deck1):
                print 'todo color'
            if self.isQuinte(deck1):
                if self.searchHighCard(deck1) == self.searchHighCard(deck2):
                    print 'DRAW'
                return self.searchHighCard(deck1) > self.searchHighCard(deck2)
            if self.isThree(deck1):
                return self.getThreeValue(deck1) > self.getThreeValue(deck2)
            if self.isTwoPair(deck1):
                print 'todo two pairs'
            if self.isOnePair(deck1):
                return self.isBetterPair(deck1, deck2)

        # search high card
        if self.searchHighCard(deck1) > self.searchHighCard(deck2):
            return True
        if self.searchHighCard(deck1) < self.searchHighCard(deck2):
            return False
        if self.searchHighCard(deck1) == self.searchHighCard(deck2):
            v = self.searchHighCard(deck1)
            to_remove = []
            for c in deck1:
                if c.value == v:
                    to_remove.append(c)
            for e in to_remove:
                deck1.remove(e)

            to_remove = []
            for c in deck2:
                if c.value == v:
                    to_remove.append(c)
            for e in to_remove:
                deck2.remove(e)

            return self.isBetterHand(deck1, deck2)

        print "lol ?!"

    def isWorseHand(self, deck1, deck2):
        """ return True is deck1 is a worse hand than deck2 """
        return not self.isBetterHand(deck1, deck2)

    def isSameHand(self, deck1, deck2):
        """ return True is deck1 is the same hand than deck2
            for now a pair is equal to a pair
            in realty a pair of as is better than a pair of 8 """
        return self.wichHand(deck1) == self.wichHand(deck2)

        return self.getThreeValue(deck1) > self.getThreeValue(deck2)

if __name__ == "__main__":
    f = open('p054_poker.txt')
    i = 0
    for l in f:
        hands = l.strip()

        hand1 = hands.split(' ')[0:5]
        hand2 = hands.split(' ')[5:10]

        # load deck 1
        deck1 = set()
        for c in hand1:
            deck1.add(Card(c[0], c[1]))

        # load deck 2
        deck2 = set()
        for c in hand2:
            deck2.add(Card(c[0], c[1]))

        poker = Poker()
        if poker.isBetterHand(deck1, deck2):
            i += 1
    print i
