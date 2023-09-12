# This class DeckOfCards includes data about the deck of cards and the following methods:
# __init__
# cards_shuffle
# deal_one
from Card import Card
import random


class DeckOfCards:
    """"This class holds information about a deck of cards and function"""

    def __init__(self):
        """This function is a constructor of a deck of cards object"""
        card_list = []
        for i in range(1, 14):
            card_list.append(Card(i, "Diamond"))
        for i in range(1, 14):
            card_list.append(Card(i, "Spade"))
        for i in range(1, 14):
            card_list.append(Card(i, "Heart"))
        for i in range(1, 14):
            card_list.append(Card(i, "Club"))
        self.card_list = card_list

    def cards_shuffle(self):
        """"This function shuffle the cards in the deco of cards"""
        random.shuffle(self.card_list)

    def __str__(self):
        """"This function return a string that represent the object"""
        str1 = ""
        for i in self.card_list:
            str1 += " " + i.__str__()
        return str1

    def deal_one(self):
        """This function return one card randomly from the deck,
            and delete him"""
        card1 = random.choice(self.card_list)
        self.card_list.remove(card1)
        return card1


