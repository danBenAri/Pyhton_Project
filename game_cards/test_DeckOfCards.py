from unittest import TestCase
from DeckOfCards import DeckOfCards
import random
from Card import Card


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test_init_valid(self):
        """A valid test case of __init__: size is 52"""
        self.assertEqual(len(self.deck.card_list), 52)

    def test_init_valid2(self):
        """A valid test case of __init__: The cards in the deck is Card object"""
        card1 = random.choice(self.deck.card_list)
        # print(card1.__dict__())
        self.assertTrue(type(card1), Card)
        print(self.deck)

    def test_cards_shuffle(self):
        """"Check that the cards_shuffle work"""
        str1 = self.deck.__str__()
        self.deck.cards_shuffle()
        str2 = self.deck.__str__()
        self.assertNotEqual(str1, str2)
        # This case may fall because the deck after the shuffle can be the same as
        # before, but the odds is not big

    def test_deal_one1(self):
        """Check the type that returns from the deal_one function"""
        card1 = self.deck.deal_one()
        self.assertTrue(type(card1), Card)

    def test_deal_one2(self):
        """check that the return card is not in the deck"""
        card1 = self.deck.deal_one()
        self.assertNotIn(card1, self.deck.card_list)
        print(card1)











