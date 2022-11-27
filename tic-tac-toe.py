PLAYER_X_TOKEN = "X"
PLAYER_0_TOKEN = "0"
EMPTY_TOKEN = ""


def run():
    startMessage()
    player1Token = ""
    player2Token = ""
    while not isValidToken(player1Token):
        player1Token = input("¿Que ficha quieres llevar X o 0? ")
        if not isValidToken(player1Token):
            print("Ficha no valida, introduce X o 0")
        player2Token = setPlayer2Token(player1Token)
    print("\n")
    player1Token = player1Token.upper()
    player2Token = player2Token.upper()
    players = ({"turn": 1, "token": "X"},
               {"turn": 2, "token": "0"})
    board = createEmptyBoard()
    board = fillAndGetBoard(board)
    renderBoard(board)
    playerTurn = 0
    endGame = False
    while not endGame:
        print("Ayuda: Escribe la fila y columna separada por un espacio")
        row, column = 0, 0
        while not isValidInput(row, column):
            position = input("Jugador " + getPlayerToken(playerTurn, players) +
                             ", ¿Posicion de tu ficha? (fila columna): ").split()
            if len(position) != 2:
                row, column = 0, 0
            else:
                row, column = position
            if not isValidInput(row, column):
                print(
                    "Error en la posición, escribe la fila y columna separada por un espacio")
        print("\n")
        row = int(row) - 1
        column = int(column) - 1
        if isValidPosition(board, row, column):
            board = fillBoardPosition(board, getPlayerToken(
                playerTurn, players), row, column)
            renderBoard(board)
            if isWinner(board, getPlayerToken(playerTurn, players)):
                print("Ganaste!!! Jugador con la ficha " +
                      getPlayerToken(playerTurn, players) + ". Felicidades")
                endGame = True
            if isTied(board):
                print("Juego empatado")
                endGame = True
        else:
            print("La posicion esta ocupada, perdiste el turno")
        playerTurn = changePlayer(playerTurn)
    print("Fin del juego")


def startMessage():
    print("Bienvenido a Tic Tac Toe (TA-TE-TI)")
    print("Autor: Harold Rivas\n")


def isValidToken(player1Token):
    return player1Token.upper() in (PLAYER_X_TOKEN, PLAYER_0_TOKEN)


def setPlayer2Token(playerToken):
    if playerToken.upper() == "X":
        return "0"
    else:
        return "X"


def createEmptyBoard():
    return [[""] * 3 for i in range(3)]


def fillAndGetBoard(board):
    tempBoard = createEmptyBoard()
    for i in range(3):
        for j in range(3):
            if (board[i][j] != ""):
                token = board[i][j]
            else:
                token = EMPTY_TOKEN
                tempBoard[i][j] = token
    return tempBoard


def renderBoard(board):
    for i in range(3):
        for j in range(3):
            token = "_" if board[i][j] == EMPTY_TOKEN else board[i][j]
            print(" | " + token, end='')
        print(" |\n")
    print("\n")


def isValidInput(row, column):
    row = int(row)
    column = int(column)
    if (row >= 1 and row <= 3) and (column >= 1 and column <= 3):
        return True
    else:
        return False


def fillBoardPosition(board, token, row, column):
    board[row][column] = token
    return board


def getPlayerToken(playerTurn, players):
    return players[playerTurn]['token']


def isValidPosition(board, row, column):
    if board[row][column] == EMPTY_TOKEN:
        return True
    else:
        return False


def isWinner(board, token):
    winner = False
    for i in range(3):
        if board[i][0] == token and board[i][1] == token and board[i][2] == token:
            winner = True
            break
        if board[0][i] == token and board[1][i] == token and board[2][i] == token:
            winner = True
            break
    if board[0][0] == token and board[1][1] == token and board[2][2] == token:
        winner = True
    if board[0][2] == token and board[1][1] == token and board[2][0] == token:
        winner = True
    return winner


def isTied(board):
    tied = False
    llenos = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY_TOKEN:
                llenos += 1
    if llenos == 9:
        tied = True
    return tied


def changePlayer(playerTurn):
    if (playerTurn == 0):
        return 1
    else:
        return 0


run()
