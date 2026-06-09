from utils import display_board

# Create ship board and bot board as hash maps
# Patrol Boat: 1, Submarine: 2, Destroyer: 3, Battleship: 4, Aircraft Carrier: 5

player_ship_board = {}
bot_board = {} # 0 means there was a guess, positive number means there is a ship, negative number means there is a hit
               # different numbers > 0 define what ship is being referenced

# Take user input to fill the user ship board with ships
def place_ships():
    print("Place your ships...")
    return 0
# Randomly place ships on board for bot
def place_bot_ships():
    return 0

# Main gameplay loop
def play_game():
    print("Target Board")
    display_board(bot_board)
    print("-----------------------------------")
    print("     1  2  3  4  5  6  7  8  9") #hardcoding border around boards for now
    print("-----------------------------------")
    display_board(player_ship_board)
    print("Your Ships")
    return 0
