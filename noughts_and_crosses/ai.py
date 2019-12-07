
def computer_first_move(grid):

    if grid[1] != 0:
        possible_moves = [5]
    elif grid[2] != 0:
        possible_moves = [5,7,9]
    elif grid[3] != 0:
        possible_moves = [5]
    elif grid[4] != 0:
        possible_moves = [3,5,9]
    elif grid[5] != 0:
        possible_moves = [1,3,7,9]
    elif grid[6] != 0:
        possible_moves = [1,5,7]
    elif grid[7] != 0:
        possible_moves = [5]
    elif grid[8] != 0:
        possible_moves = [1,3,5]
    elif grid[9] != 0:
        possible_moves = [5]

    return possible_moves

def computer_second_move(grid):

    possible_moves = []
    
    # If the human has gone in two opposite corners, then if the computer's next turn is in a corner then it is going to lose
    # So this check means that it will not go in a corner in this situation, and mean it has the best chance of winning
    if (grid[1]=="X") and (grid[9]=="X") or (grid[3]=="X") and (grid[7]=="X"):
        possible_moves = [2,4,6,8]

    # If the human has had two moves and all the symbols are in a diagonal line, then the computer should go in one of the 
    # remaining corners, otherwise it is making a move that will mean it loses, and mean it has the best chance of winning
    if (grid[1]=="X") and (grid[5]=="X") and (grid[9]=="O"):
        possible_moves = [3,7]
    if (grid[3]=="X") and (grid[5]=="X") and (grid[7]=="O"):
        possible_moves = [1,9]
    if (grid[7]=="X") and (grid[5]=="X") and (grid[3]=="O"):
        possible_moves = [1,9]
    if (grid[9]=="X") and (grid[5]=="X") and (grid[1]=="O"):
        possible_moves = [3,7]

    return possible_moves

def computer_win_move(grid):
    
    chosen_move = None

    # For each of the 9 grid squares, check to see if it has to be played for the computer to win the game
    # But also make sure that this grid square hasn't already been played first as well
    if((grid[2]=="O" and grid[3]=="O") or (grid[4]=="O" and grid[7]=="O") or (grid[5]=="O" and grid[9]=="O")) and (grid[1] != "X") and (grid[1] != "O"):
            chosen_move = 1
    elif((grid[1]=="O" and grid[3]=="O") or (grid[5]=="O" and grid[8]=="O")) and (grid[2] != "X") and (grid[2] != "O"):
            chosen_move = 2
    elif((grid[1]=="O" and grid[2]=="O") or (grid[6]=="O" and grid[9]=="O") or (grid[5]=="O" and grid[7]=="O")) and (grid[3] != "X") and (grid[3] != "O"):
            chosen_move = 3
    elif((grid[1]=="O" and grid[7]=="O") or (grid[5]=="O" and grid[6]=="O")) and (grid[4] != "X") and (grid[4] != "O"):
            chosen_move = 4
    elif((grid[1]=="O" and grid[9]=="O") or (grid[2]=="O" and grid[8]=="O") or (grid[3]=="O" and grid[7]=="O") or (grid[4]=="O" and grid[6]=="O")) and (grid[5] != "X") and (grid[5] != "O"):
            chosen_move = 5
    elif((grid[3]=="O" and grid[9]=="O") or (grid[4]=="O" and grid[5]=="O")) and (grid[6] != "X") and (grid[6] != "O"):
            chosen_move = 6
    elif((grid[1]=="O" and grid[4]=="O") or (grid[8]=="O" and grid[9]=="O") or (grid[3]=="O" and grid[5]=="O")) and (grid[7] != "X") and (grid[7] != "O"):
            chosen_move = 7
    elif((grid[2]=="O" and grid[5]=="O") or (grid[7]=="O" and grid[9]=="O")) and (grid[8] != "X") and (grid[8] != "O"):
            chosen_move = 8
    elif((grid[3]=="O" and grid[6]=="O") or (grid[1]=="O" and grid[5]=="O") or (grid[7]=="O" and grid[8]=="O")) and (grid[9] != "X") and (grid[9] != "O"):
            chosen_move = 9

    return chosen_move

def computer_block_move(grid):
    
    chosen_move = None

    # For each of the 9 grid squares, check to see if it has to be played to block the player from winning
    # But also make sure that this grid square hasn't already been played first as well
    if((grid[2]=="X" and grid[3]=="X") or (grid[4]=="X" and grid[7]=="X") or (grid[5]=="X" and grid[9]=="X")) and (grid[1] != "X") and (grid[1] != "O"):
            chosen_move = 1
    elif((grid[1]=="X" and grid[3]=="X") or (grid[5]=="X" and grid[8]=="X")) and (grid[2] != "X") and (grid[2] != "O"):
            chosen_move = 2
    elif((grid[1]=="X" and grid[2]=="X") or (grid[6]=="X" and grid[9]=="X") or (grid[5]=="X" and grid[7]=="X")) and (grid[3] != "X") and (grid[3] != "O"):
            chosen_move = 3
    elif((grid[1]=="X" and grid[7]=="X") or (grid[5]=="X" and grid[6]=="X")) and (grid[4] != "X") and (grid[4] != "O"):
            chosen_move = 4
    elif((grid[1]=="X" and grid[9]=="X") or (grid[2]=="X" and grid[8]=="X") or (grid[3]=="X" and grid[7]=="X") or (grid[4]=="X" and grid[6]=="X")) and (grid[5] != "X") and (grid[5] != "O"):
            chosen_move = 5
    elif((grid[3]=="X" and grid[9]=="X") or (grid[4]=="X" and grid[5]=="X")) and (grid[6] != "X") and (grid[6] != "O"):
            chosen_move = 6
    elif((grid[1]=="X" and grid[4]=="X") or (grid[8]=="X" and grid[9]=="X") or (grid[3]=="X" and grid[5]=="X")) and (grid[7] != "X") and (grid[7] != "O"):
            chosen_move = 7
    elif((grid[2]=="X" and grid[5]=="X") or (grid[7]=="X" and grid[9]=="X")) and (grid[8] != "X") and (grid[8] != "O"):
            chosen_move = 8
    elif((grid[3]=="X" and grid[6]=="X") or (grid[1]=="X" and grid[5]=="X") or (grid[7]=="X" and grid[8]=="X")) and (grid[9] != "X") and (grid[9] != "O"):
            chosen_move = 9

    return chosen_move