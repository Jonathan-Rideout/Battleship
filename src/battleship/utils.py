# Function to display a given board
def display_board(board):
    for i in range(1, 10): # rows
        row = chr(i + 64)
        print(f"{row} |  ", end = "")
        for col in range(1, 10): # columns
            print(f"{board.get(f"{row}{col}", 0)}", " ", end = "")
        print("|")
    return 0

def bounds_check(coord, direction, ship_len):
    letter_val = ord(list(coord)[0]) - 64 # Converts to numerical ascii value and subtracts down
    num_val = int(list(coord)[1])

    match direction:
        case "up":
            if letter_val - ship_len <= 0: # Letters increase downwards, so a ship placed at B (2) going up would need to be checked against 0 with subtraction
                return 1
            else:
                return 0
        case "down":
            if letter_val + ship_len > 9:
                return 1
            else:
                return 0
        case "left":
            if num_val - ship_len <= 0:
                return 1
            else:
                return 0
        case "right":
            if num_val + ship_len > 9:
                return 1
            else:
                return 0
    return 1
            

def collision_check(coord, direction, ship_len, board):

    # increase coordinate by direction in loop
    #   if value exists, fail
    
    letter = list(coord)[0]
    num = int(list(coord)[1])

    match direction:
        case "up":
            next_coord = letter + str(num)
            for _ in range(0, ship_len):
                if board.get(next_coord) is None:
                    letter = str(ord(letter) - 1)
                else:
                    return 1
            return 0
        case "down":
            next_coord = letter + str(num)
            for _ in range(0, ship_len):
                if board.get(next_coord) is None:
                    letter = str(ord(letter) + 1)
                else:
                    return 1
            return 0
        case "left":
            next_coord = letter + str(num)
            for _ in range(0, ship_len):
                if board.get(next_coord) is None:
                    num -= 1 
                else:
                    return 1
            return 0
        case "right":
            next_coord = letter + str(num)
            for _ in range(0, ship_len):
                if board.get(next_coord) is None:
                    num += 1 
                else:
                    return 1
            return 0

    return 1


