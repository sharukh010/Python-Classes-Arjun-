import tabulate # pip install tabulate 

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
turn = True # True -> X's turn , False -> O's trun 
count = 0 # number of occupied cells 

def display_board(): 
    table = tabulate.tabulate(board,headers="firstrow",tablefmt="grid")
    print("Board:")
    print(table)

def is_empty(board,row,col): 
    if board[row][col] == " ": 
        return True 
    else: 
        return False 

def is_safe(board,row,col): 
    if row<len(board) and col < len(board[row]) and row >= 0 and col >= 0: 
        return True 
    else: 
        return False

def is_tie():
    if count == 9: 
        return True 
    else: 
        return False 
def is_winner(board,marker): 
    # checking in the rows 
    for row in range(len(board)): 
        if board[row][0] == board[row][1] == board[row][2] == marker: 
            return True 

    # checking in the columns 
    for col in range(len(board[0])): 
        if board[0][col] == board[1][col] == board[2][col] == marker: 
            return True 

    if board[0][0] == board[1][1] == board[2][2] == marker: 
        return True 
    if board[0][2] == board[1][1] == board[2][0] == marker: 
        return True
     
    return False 
    
marker = "X" if turn else "O"
while True: 
    display_board()
    if is_winner(board,marker): 
        print(f"{marker} has won the game")
        break 
    elif is_tie(): 
        print(f"It's a tie.")
        break 
    marker = "X" if turn else "O"
    """
    if turn: 
        marker = "X"
    else: 
        marker = "O"
    """
    # value-1 if condition else Value-2 
    # if the condition is true value-1 will be stored 
    # if condition is false value-2 will be stored 
    print(f"{marker}'s Turn: ")
    row = int(input("Enter row number: "))
    col = int(input("Enter col number: "))
    if is_safe(board,row-1,col-1): 
        if is_empty(board,row-1,col-1): 
            board[row-1][col-1] = marker 
            count += 1 
            turn = not turn  # not True -> False , not False -> True 
        else: 
            print(f"Position ({row},{col}) is already occupied")
    else:
        print(f"Marker cannot be placed at ({row},{col})") 