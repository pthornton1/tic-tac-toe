# Steps to do
# 1. Welcome player
# 2. Draw board
# 3. Ask player where they want to place their mark
# 4. Check if anyone has won
# 5. Ask next player where they want to place mark

move_dict = {}

def print_board():
    board = ""
    for y in range(0,3):
        row = ""
        for x in range(0,3):
            if (x+1,y+1) in move_dict:
                row += f" {move_dict[(x+1,y+1)]} "
            else:
                row += "   "
            if x < 2:
                row += "|"
        board += row
        if y < 2:
            board += "\n-----------\n"
    print(board)

def take_turn(move_dict, player_num):
    if player_num == 1:
        marker = 'X'
    else:
        marker = 'O'
    player_choice = input(f"Player {player_num}: You are '{marker}'. Where do you want to move? Type the x,y coordinates seperated with a comma. Eg. '2,2' for the centre: ")
    coords = player_choice.split(',')
    coords = tuple([int(coord) for coord in coords])
    move_dict[coords] = marker
    return move_dict

def check_for_win():

    # check each row and column and diagonal
    X_col_total = [0,0,0]
    O_col_total = [0,0,0] 
    
    diagonal_1_X = 0
    diagonal_1_O = 0
    diagonal_1_coords = [(1,1), (2,2), (3,3)]
    
    diagonal_2_X = 0
    diagonal_2_O = 0
    diagonal_2_coords = [(3,1), (2,2), (1,3)]
    
    for row in range (1,4):
        
        for col in range (1,4):
            X_row_total = 0
            O_row_total = 0      
            if (col,row) in move_dict:
                # Add rows and columns
                if move_dict[(col,row)] == 'X':
                    X_row_total += 1
                    X_col_total[col-1] += 1
                    if (col,row) in diagonal_1_coords:
                        diagonal_1_X += 1
                    if (col,row) in diagonal_2_coords:
                        diagonal_2_X += 1  
                else:
                    O_row_total += 1
                    O_col_total[col-1] += 1
                    if (col,row) in diagonal_1_coords:
                        diagonal_1_O += 1
                    if (col,row) in diagonal_2_coords:
                        diagonal_2_O += 1  
        if X_row_total == 3:
            return True, 1
        if O_row_total == 3:
            return True, 2
        
    # Check column totals
    for num in X_col_total:
        if num == 3:
            return True, 1
        
    for num in O_col_total:
        if num == 3:
            return True, 2
    
    # Check diagonal totals
    if diagonal_1_X == 3 or diagonal_2_X == 3:
            return True, 1
    
    if diagonal_1_O == 3 or diagonal_2_O == 3:
            return True, 2
                    
    else:
        return False, 0

won, winner = False, 0
player_turn = 1 

print("Welcome to Tic Tac Toe!")
print_board()

while not won: 
    move_dict = take_turn(move_dict, player_turn)
    print_board()
    won, winner = check_for_win()
    if player_turn == 1:
        player_turn = 2
    else:
        player_turn = 1
        
    if won:
        print(f"Player {winner} won!")
    


