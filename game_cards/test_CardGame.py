from unittest import TestCase
from CardGame import CardGame
from DeckOfCards import DeckOfCards
from Card import Card
from Player import Player


class TestCardGame(TestCase):
    def setUp(self):
        self.game1 = CardGame("Daniel", "Ron", 16, 16)

    def test__init__valid(self):
        """"A valid case of an init function"""
        self.assertEqual("Daniel", self.game1.player1.name)
        self.assertEqual("Ron", self.game1.player2.name)
        self.assertEqual(16, self.game1.player1.num_of_cards)
        self.assertEqual(16, self.game1.player2.num_of_cards)

    def test__init__invalid1(self):
        """"An invalid case of init function: Type Error"""
        with self.assertRaises(TypeError):
            game2 = CardGame(293, "ron", 16, 16)
        with self.assertRaises(TypeError):
            game2 = CardGame("daniel", [1, 2, 3], 16, 16)
        with self.assertRaises(TypeError):
            game2 = CardGame("daniel", "ron", "16", 16)
        with self.assertRaises(TypeError):
            game2 = CardGame("daniel", "ron", 16, "16")

    def test__init__invalid2(self):
        """"An invalid case of init function: name isn't only with letters"""
        game2 = CardGame("383kasa", "daniel", 18, 18)
        self.assertEqual("Unnamed", game2.player1.name)

    def test_new_game_valid(self):
        """"A valid test to check if the hands of the player has been sets"""
        self.assertEqual(len(self.game1.player1.player_deck_list), self.game1.player1.num_of_cards)
        self.assertEqual(len(self.game1.player2.player_deck_list), self.game1.player2.num_of_cards)

    def test_new_game_invalid(self):
        """"Check if we call the new_game functino not from init gets error"""
        with self.assertRaises(RuntimeError):
            self.game1.new_game()

    def test_get_winner_valid1(self):
        """"A valid case: this player is the winner"""
        self.game1.player2.get_card()
        self.assertEqual(self.game1.get_winner(), self.game1.player1)

    def test_get_winner_valid2(self):
        """"A valid case: the other player is the winner"""
        self.game1.player1.get_card()
        self.assertEqual(self.game1.get_winner(), self.game1.player2)

    def test_get_winner_valid3(self):
        """"A valid case: both players with the same len of cards in hands"""
        self.assertIsNone(self.game1.get_winner())

