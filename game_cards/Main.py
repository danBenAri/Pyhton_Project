from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player
from CardGame import CardGame


player1_name = input("Please enter the first player name: ")
player2_name = input("Please enter the second player name: ")
game = CardGame(player1_name, player2_name)

print(f"{player1_name} hand is: {game.player1} \n")
print(f"{player2_name} hand is: {game.player2} \n")

for i in range(10):
    self_card = game.player1.get_card()
    other_card = game.player2.get_card()

    if self_card > other_card:
        game.player1.add_card(self_card)
        game.player1.add_card(other_card)
        print(f"{player1_name} is the winner of {i+1} round!"
              f"\n{player1_name} card is: {self_card}"
              f"\n{player2_name} card is: {other_card}\n")
    else:
        game.player2.add_card(self_card)
        game.player2.add_card(other_card)
        print(f"{player2_name} is the winner of {i+1} round!"
              f"\n{player1_name} card is: {self_card}"
              f"\n{player2_name} card is: {other_card}\n")
if game.get_winner() == game.player1:
    print(f"----------------{player1_name} is the winner of this game!!!!!!!!!!!!--------------------------\n"
          f"{player1_name} number of cards in hand: {len(game.player1.player_deck_list)}\n"
          f"{player2_name} number of cards in hand: {len(game.player2.player_deck_list)}\n")
elif game.get_winner() == game.player2:
    print(f"----------------{player2_name} is the winner of this game!!!!!!!!!!!!--------------------------\n"
          f"{player1_name} number of cards in hand: {len(game.player1.player_deck_list)}\n"
          f"{player2_name} number of cards in hand: {len(game.player2.player_deck_list)}\n")
else:
    print("This game ended in a draw...")