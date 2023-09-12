from DeckOfCards import DeckOfCards
from Player import Player


class CardGame:
    """"This class holds information about a class game data and functions"""
    global_flag = False

    def __init__(self, player_name1: str, player_name2: str, num_of_cards1=26, num_of_cards2=26):
        if type(player_name1) != str or type(player_name2) != str:
            raise TypeError("Player name must be string!")
        if type(num_of_cards1) != int or type(num_of_cards2) != int:
            raise TypeError("Number of cards must be int!")

        self.game_deck = DeckOfCards()
        player1 = Player(player_name1, num_of_cards1)
        player2 = Player(player_name2, num_of_cards2)
        self.player1 = player1
        self.player2 = player2
        global global_flag
        global_flag = False
        self.new_game()
        global_flag = True

    def new_game(self):
        """"This function shuffle the deck and set hands for the players"""
        global global_flag
        if global_flag:
            raise RuntimeError("You cannot start a new game after starting a game!")
        else:
            self.game_deck.cards_shuffle()  # shuffle the deck
            self.player1.set_hand(self.game_deck)  # set the hand for player 1
            self.player2.set_hand(self.game_deck)  # set the hand for player 2

    def get_winner(self):
        """"Return the winner of this game"""
        if len(self.player1.player_deck_list) > len(self.player2.player_deck_list):
            return self.player1
        elif len(self.player1.player_deck_list) < len(self.player2.player_deck_list):
            return self.player2
        else:
            return None



