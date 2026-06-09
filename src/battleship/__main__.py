from core import play_game
print("Battleship")
print("Enter 1 for a game tutorial")
print("Enter 2 to start the game")

input = int(input())

if input == 1:
    print("Game tutorial goes here")
if input == 2:
    play_game()


