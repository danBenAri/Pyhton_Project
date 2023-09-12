from unittest import TestCase
from Card import Card


class TestCard(TestCase):

    def setUp(self):
        self.card = Card(12,"Diamond")
        self.card_edge = Card(1, "Club")

    def test_init_valid(self):
        """A valid test case of __init__"""
        self.assertEqual(12,self.card.value)
        self.assertEqual("Diamond",self.card.suit)

    def test_init_valid1(self):
        """A valid test case of __init__"""
        self.assertEqual(1, self.card_edge.value)
        self.assertEqual("Club",self.card_edge.suit)

    def test_init_invalid_value(self):
        """ A test case of an invalid value """
        with self.assertRaises(TypeError):
            card1 = Card("13","Spade")
        with self.assertRaises(ValueError):
            card2 = Card(15, "Club")

    def test_init_invalid_suit(self):
        """ A test case of an invalid suit """
        with self.assertRaises(TypeError):
            card1 = Card(12,12)
        with self.assertRaises(ValueError):
            card2 = Card(12, "skjdf")

    def test_get_value_by_suit_valid(self):
        """"A test case of a valid suit for the function"""
        self.assertEqual(1, self.card.get_value_by_suit())

    def test_get_value_by_suit_invalid(self):
        """"A test case of an invalid suit for the function"""
        with self.assertRaises(ValueError):
            card1 = Card(12, "clown")

    def test__gt__valid1(self):
        """A test case of comparing two cards: different values and different suits"""
        card1 = Card(10, "Diamond")
        card2 = Card(12, "Club")
        self.assertFalse(card1 > card2)

    def test__gt__valid2(self):
        """A test case of comparing two cards: different values one with 1 and different suits"""
        card1 = Card(1, "Diamond")
        card2 = Card(12, "Club")
        self.assertTrue(card1 > card2)

    def test__gt__valid3(self):
        """A test case of comparing two cards: different values one with 1 and same suits"""
        card1 = Card(13, "Diamond")
        card2 = Card(12, "Club")
        self.assertTrue(card1 > card2)

    def test__gt__valid4(self):
        """A test case of comparing two cards: same values and different suits"""
        card1 = Card(12, "Diamond")
        card2 = Card(12, "Club")
        self.assertFalse(card1 > card2)

    def test__gt__valid5(self):
        """A test case of comparing two cards: same values and same suits"""
        card1 = Card(12, "Diamond")
        card2 = Card(12, "Diamond")
        self.assertFalse(card1 > card2)

    def test__gt__invalid(self):
        """"An invalid test case of gt function"""
        with self.assertRaises(TypeError):
            card2 = [13, "Heart"]
            self.card > card2

    def test__eq__valid1(self):
        """"A valid test case of eq function"""
        card1 = Card(12, "Spade")
        card2 = Card(12, "Spade")
        self.assertTrue(card1 == card2)

    def test__eq__valid2(self):
        """"A invalid test case of eq function: the value is different"""
        card1 = Card(13, "Spade")
        card2 = Card(12, "Spade")
        self.assertFalse(card1 == card2)

    def test__eq__valid3(self):
        """"A invalid test case of eq function: the suit is different"""
        card1 = Card(13, "Spade")
        card2 = Card(13, "Heart")
        self.assertFalse(card1 == card2)

    def test__eq__invalid(self):
        """"An invalid test case of eq function"""
        with self.assertRaises(TypeError):
            card2 = [13, "Heart"]
            self.card == card2








