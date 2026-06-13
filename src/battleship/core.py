from utils import bounds_check, collision_check, display_board

# Create ship board and bot board as hash maps
# Patrol Boat: 1, Submarine: 2, Destroyer: 3, Battleship: 4, Aircraft Carrier: 5
player_ship_board = {}
bot_board = {} # 0 means there was a guess, positive number means there is a ship, negative number means there is a hit
               # different numbers > 0 define what ship is being referenced
ships = {} # Tracks ship placements and health
           # Negative means enemy ship
ship_lengths = {1 : 2, 2 : 3, 3 : 3, 4 : 4, 5 : 5}
# Take user input to fill the user ship board with ships
def place_ships():
    
    print("Place your ships...")
    
    placement_count = 0
    
    while placement_count < 5: # todo - add input validation
        print("letter then number, like 'A5'")
        coord = input("Type in a coordinate: ")
        print("up, down, left, right")
        direction = input("Type in the direction the ship should grow form this coordinate: ")
        print("Patrol Boat: 1, Submarine: 2, Destroyer: 3, Battleship: 4, Aircraft Carrier: 5")
        ship_id = input("Type in the ship ID to be placed: ")

        ship_len = ship_lengths[int(ship_id)]
        
        if bounds_check(coord, direction, ship_len) and collision_check(coord, direction, ship_len, player_ship_board):
            #place ships
            
            letter = list(coord)[0]
            num = int(list(coord)[1])

            match direction:
                case "up":
                    for _ in range(0, ship_len):
                        next_coord = letter + str(num)
                        print(next_coord)
                        player_ship_board[next_coord] = ship_id
                        letter = chr(ord(letter) - 1)
                case "down":
                    for _ in range(0, ship_len):
                        next_coord = letter + str(num)
                        player_ship_board[next_coord] = ship_id
                        letter = chr(ord(letter) + 1)
                case "left":
                    for _ in range(0, ship_len):
                        next_coord = letter + str(num)
                        player_ship_board[next_coord] = ship_id
                        num -= 1
                case "right":
                    for _ in range(0, ship_len):
                        next_coord = letter + str(num)
                        player_ship_board[next_coord] = ship_id
                        num += 1

        #temp
        display_board(player_ship_board)



    return 1

# Randomly place ships on board for bot
def place_bot_ships():
    return 1

# Main gameplay loop
def play_game():
    # For now the board layout is hardcoded
    print("Target Board")
    display_board(bot_board)
    print("-----------------------------------")
    print("     1  2  3  4  5  6  7  8  9")
    print("-----------------------------------")
    display_board(player_ship_board)
    print("Your Ships")

    place_ships()
    place_bot_ships()




    
    return 1
