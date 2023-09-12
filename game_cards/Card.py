# This class Card includes data about the card and the following methods:
# __init__
# __eq__
# __gt__
class Card:
    """This class holds information and functions about Card"""

    def __init__(self, value=type[int], suit=type[str]):
        """"This function is a constructor of a card object"""

        # Check if the types at the arguments are corrects
        if type(value) != int:
            raise TypeError("Value must be type int!")
        if type(suit) != str:
            raise TypeError("Suit must be type string!")
        if value < 1 or value > 13:
            raise ValueError("Value must be between 1-13")

        self.value = value  # if we got here the value is valid
        if suit in ["Diamond", "Spade", "Heart", "Club"]:  # then the suit is valid
            self.suit = suit
        else:
            raise ValueError("Suit must be Diamond/Spade/Heart/Club")

    def get_value_by_suit(self):  # A helper function for the __gt__ function
        """"This function return value according to the suit of the card"""
        suit1 = self.suit
        if suit1 == "Diamond":
            return 1
        elif suit1 == "Spade":
            return 2
        elif suit1 == "Heart":
            return 3
        elif suit1 == "Club":
            return 4
        else:
            raise ValueError("Suit must be Diamond/Spade/Heart/Club ")

    def __gt__(self, other):
        """Compare between Cards according to their value
        If they have the same value then we compare them according to the suit"""

        # Check if the type at the arguments is correct
        if type(other) != Card:
            raise TypeError("Other must be Card object!")

        if self.value == other.value:  # we compare according to the suits
            self_new_value = self.get_value_by_suit()
            other_nem_value = other.get_value_by_suit()
            if self_new_value > other_nem_value:
                return True
            else:
                return False

        if self.value == 1 and other.value != 1:  # 1 is Ace and he is the most powerful value
            return True
        elif self.value != 1 and other.value == 1:  # 1 is Ace and he is the most powerful value
            return False
        else:  # This case is when the cards have different values and none of them is 1
            if self.value > other.value:
                return True
            else:
                return False

    def __eq__(self, other):
        """Compare a Card according to its value and suit
            Check if the type at the argument is valid"""
        if type(other) != Card:
            raise TypeError("Other must be a card object! ")

        return self.value == other.value and self.suit == other.suit

    def __str__(self):
        value = self.value
        if value == 1:
            value = "Ace"
        elif value == 11:
            value = "Prince"
        elif value == 12:
            value = "Queen"
        elif value == 13:
            value = "King"
        return f"[{value}, {self.suit}]"

