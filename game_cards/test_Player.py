from unittest import TestCase
from Player import Player
from DeckOfCards import DeckOfCards
from Card import Card
from unittest import mock


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("Dani", 24)
        self.deck = DeckOfCards()
        self.player.set_hand(self.deck)

    def test_init_valid(self):
        """A valid test case of __init__: name and number of cards is initialize correct"""
        self.assertEqual("Dani", self.player.name)
        self.assertEqual(24, self.player.num_of_cards)

    def test_init_valid2(self):
        """A valid test case of __init__: number of cards is out range, and without number of cards"""
        player1 = Player("Ron", 29)
        self.assertEqual(26, player1.num_of_cards)
        player2 = Player("Dvir")
        self.assertEqual(26, player2.num_of_cards)

    def test_init_valid3(self):
        """A valid test case of __init__: name is not only letters"""
        player1 = Player("Ro2n#", 29)
        self.assertEqual("Unnamed", player1.name)

    def test_init_valid4(self):
        """A valid test case of __init__: edge values"""
        player1 = Player("Ron", 25)
        self.assertEqual(25, player1.num_of_cards)
        player2 = Player("Dvir", 10)
        self.assertEqual(10, player2.num_of_cards)

    def test_init_invalid(self):
        """A valid test case of __init__: name with invalid type"""
        with self.assertRaises(TypeError):
            player1 = Player(["d", "a", "a"], 18)

    def test_init_invalid2(self):
        """A valid test case of __init__: name with invalid type"""
        with self.assertRaises(TypeError):
            player1 = Player("dani", (1,2,3,4,5))

    def test_set_hand_valid(self):
        """"A valid test case of set_hand: check if the len of the player deck is with the same
        len of number of cards"""
        self.assertEqual(len(self.player.player_deck_list), self.player.num_of_cards)

    def test_set_hand_valid2(self):
        """"A valid test case of set_hand: check if the type of element in the player
        Deck is a Card object"""
        self.assertTrue(type(self.player.player_deck_list[0]) == Card)

    def test_set_hand_invalid(self):
        """"A invalid case of set_hand: input deck is with invalid type"""
        with self.assertRaises(TypeError):
            deck = [1, 2, 3]
            self.player.set_hand(deck)

    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value=Card(12, "Spade"))
    def test_set_hand_invalid2(self, mock_rand_numbers):
        player1 = Player("ron", 10)
        player1.set_hand(self.deck)
        self.assertEqual(12, player1.player_deck_list[0].value)
        self.assertEqual("Spade", player1.player_deck_list[0].suit)

    def test_get_card(self):
        """"A valid case of get_card"""
        card1 = self.player.get_card()
        self.assertNotIn(card1, self.player.player_deck_list)
        self.assertTrue(type(card1) == Card)

    def test_add_card_valid(self):
        """"A valid case of add_card function: check if the card added to the player deck"""
        card1 = Card(1, "Heart")
        player1 = Player("David", 10)
        player1.add_card(card1)
        self.assertIn(card1, player1.player_deck_list)

    def test_add_card_invalid(self):
        """"An invalid case of add_card: get invalid input as a card to add"""
        player1 = Player("David", 10)
        with self.assertRaises(TypeError):
            player1.add_card({1: "Heart"})

