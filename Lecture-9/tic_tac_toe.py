import tabulate # pip install tabulate 

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
turn = True # True -> X's turn , False -> O's trun 
while True: 
    table = tabulate.tabulate(board,headers="firstrow",tablefmt="grid")
    print("Board:")
    print(table)
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
    board[row-1][col-1] = marker 
    turn = not turn  # not True -> False , not False -> True 