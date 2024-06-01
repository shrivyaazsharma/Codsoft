import random

print("________________________________________")
print("\nWelcome to the Tic-Tac-Toe game ! ..... ")
print("________________________________________")

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

def printgameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], end=" |")
    print("\n+---+---+---+")

def modify_Array(num, turn):
    num -= 1
    if num == 0:
        gameBoard[0][0] = turn
    elif num == 1:
        gameBoard[0][1] = turn
    elif num == 2:
        gameBoard[0][2] = turn
    elif num == 3:
        gameBoard[1][0] = turn
    elif num == 4:
        gameBoard[1][1] = turn
    elif num == 5:
        gameBoard[1][2] = turn
    elif num == 6:
        gameBoard[2][0] = turn
    elif num == 7:
        gameBoard[2][1] = turn
    elif num == 8:
        gameBoard[2][2] = turn

def Check_for_Winner(gameBoard):
    # Vertical checks
    for col in range(3):
        if gameBoard[0][col] == gameBoard[1][col] == gameBoard[2][col]:
            if gameBoard[0][col] == 'X' or gameBoard[0][col] == 'O':
                return gameBoard[0][col]

    # Horizontal checks
    for row in range(3):
        if gameBoard[row][0] == gameBoard[row][1] == gameBoard[row][2]:
            if gameBoard[row][0] == 'X' or gameBoard[row][0] == 'O':
                return gameBoard[row][0]

    # Diagonal checks
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]:
        if gameBoard[0][0] == 'X' or gameBoard[0][0] == 'O':
            return gameBoard[0][0]

    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]:
        if gameBoard[0][2] == 'X' or gameBoard[0][2] == 'O':
            return gameBoard[0][2]

    return None  # No winner yet

def minimax(board, depth, isMaximizing):
    winner = Check_for_Winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif not any(isinstance(i, int) for row in board for i in row):
        return 0

    if isMaximizing:
        bestScore = float('-inf')
        for i in range(3):
            for j in range(3):
                if isinstance(board[i][j], int):
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = (i * 3) + (j + 1)
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for i in range(3):
            for j in range(3):
                if isinstance(board[i][j], int):
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = (i * 3) + (j + 1)
                    bestScore = min(score, bestScore)
        return bestScore

def bestMove():
    bestScore = float('-inf')
    move = 0
    for i in range(3):
        for j in range(3):
            if isinstance(gameBoard[i][j], int):
                gameBoard[i][j] = 'O'
                score = minimax(gameBoard, 0, False)
                gameBoard[i][j] = (i * 3) + (j + 1)
                if score > bestScore:
                    bestScore = score
                    move = (i * 3) + (j + 1)
    return move

leaveLoop = False
turnCounter = int(input("\nEnter '1' to Start First or '0' to go with Second:" ))

def declaration():
    winner = Check_for_Winner(gameBoard)
    if winner is not None:
        printgameBoard()
        print(f"{winner} Wins! Game Over")
        return True
    elif not possibleNumbers:  # Check for tie
        printgameBoard()
        print("The match is a Tie. Game Over")
        return True
    return False

while not leaveLoop:
    if not declaration():
        if turnCounter % 2 == 1:
            printgameBoard()
            number_picked = int(input("\nEnter the slot no: "))
            print("___________________")
            if 1 <= number_picked <= 9 and number_picked in possibleNumbers:
                modify_Array(number_picked, 'X')
                possibleNumbers.remove(number_picked)
            else:
                print("Invalid Input!..")
                continue
            turnCounter += 1
        else:
            cpu_Choice = bestMove()
            print("\nCpu Choice:", cpu_Choice)
            print("________________________")
            modify_Array(cpu_Choice, 'O')
            possibleNumbers.remove(cpu_Choice)
            turnCounter += 1
    else:
        leaveLoop = True
