
board = [[2,9,0,7,0,0,0,0,1],
         [0,4,0,0,5,9,0,2,7],
         [0,0,0,3,0,0,9,0,8],
         [3,1,0,9,2,0,8,5,0],
         [0,0,0,0,0,0,1,9,0],
         [0,8,0,1,0,0,7,3,0],
         [7,3,4,0,9,0,6,0,5],
         [0,0,6,0,0,7,0,1,3],
         [8,2,1,5,3,0,0,7,0]]

#function to print the sudoku board
def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("___________________")

        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print('|', end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')

#to print the board to be solved
print('Soduku board: \n')
print_board(board)

#Checks if it is possible to assign a num in the empty space
def isAllowed(board, row, col, num):
    #Checks if the same num is in the row 
    for x in range(len(board)):
        if board[row][x] == num:
            return False

    #Checks if the same num is in the column
    for x in range(len(board)):
        if board[x][col] == num:
            return False

    #checks if the same num is in the 3*3 matrix
    maRow = row - row%3
    maCol = col - col%3

    for i in range(3):
        for j in range(3):
            if board[i + maRow][j + maCol] == num:
                return False
    return True

#assign values to all unassigned locations in such a way to meet the requirements for sudoku solution
def solve(board, row, col):
    #return true to avoid backtracking if 
    #we reached the 8th row and 9th matrix the end.
    if (row == len(board) - 1 and col == len(board)):
        return True
    
    #if column == 9 then we move to the next row and so column start from 0
    if col == len(board):
        row +=1
        col = 0

    #checks if the current position is not empty 
    # we iterate for next column 
    if board[row][col] > 0:
        return solve(board, row, col+1) 
    for num in range(1, len(board) + 1, 1):
        #checks if it is allowed to place the num(1-9) 
        #in the given row,col > move to next column
        if isAllowed(board,row,col,num):
            #assigning the num in the current position 
            #and assume it is correct
            board[row][col] = num
            #checks the next column possibility
            if solve(board,row,col+1):
                return True
        
        #removing the assigned num, (the assumption was wrong)
        #and we continue with the next aaumption with diff num
        board[row][col] = 0
    return False

if (solve(board, 0, 0)):
    print('\n Solved board: \n')
    print_board(board)
else:
    print("no solution exists")