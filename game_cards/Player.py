# This class Player includes data about the Player and the following methods:
# __init__
# set_hand
# get_card
# add_card

from Card import Card
from DeckOfCards import DeckOfCards
import random

class Player:
    """"This class holds information about Player information and methods"""

    def __init__(self, name: str, num_of_cards=26):
        """"This is a constructor function of a player object"""
        if type(name) != str:
            raise TypeError("Name must be string!")
        if type(num_of_cards) != int:
            raise TypeError("Number of cards must be int!")

        self.player_deck_list = []
        if name.isalpha():
            self.name = name
        else:
            self.name = "Unnamed"
        if 10 <= num_of_cards <= 26:
            self.num_of_cards = num_of_cards
        else:
            self.num_of_cards = 26

    def set_hand(self, deck: DeckOfCards):
        """"This function gets deck of cards object, and give
            To the player random cards from there, according to the number of cards that this
            Player need to get"""
        if type(deck) != DeckOfCards:
            raise TypeError("Deck must be DecoOfCards object!")
        for i in range(self.num_of_cards):
            self.player_deck_list.append(deck.deal_one())

    def get_card(self):
        """"This function randomly choose card from the player hand, delete from his deck and return it"""
        card1 = random.choice(self.player_deck_list)
        self.player_deck_list.remove(card1)
        return card1

    def add_card(self, card: Card):
        """"This function get card and ass him to the player deck"""
        if type(card) != Card:
            raise TypeError("Card must be Card object!")

        self.player_deck_list.append(card)

    def __str__(self):
        """"This function return a string that represent the object"""
        str1 = ""
        for i in self.player_deck_list:
            str1 += "\n" + i.__str__()
        return str1

