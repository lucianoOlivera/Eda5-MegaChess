class MovesBoard():
    moveline = []
    movediagonal = []
    movelineenemy = []
    movediagonalenemy = []
    def moveLine(self,dir,board,piece):
        """

        Resuelve la cantidad de espacio libre entre un pieza origen para poder hacer un movimiento en linea de espacio libre

        Devuelve la pieza destino que está situada a una distancia n espacio “ ” antes de otra pieza diferente a  “ ”

        parámetro
        dir----> Es la dirección donde va resolver
        board----> Tablero del turno
        piece----> pieza origen

        """
        for i in range(0,len(board)):
            if (board[i].get_row() == piece.get_row() and board[i].get_column() == piece.get_column()) and 0<board[i].get_column()<15 and 0<board[i].get_row()<15:
                if dir == 'up':
                    self.moveline.clear()
                    if board[i + 16].get_name() == " ":
                        MovesBoard().moveLine(dir,board,board[i + 16])
                        self.moveline.append(board[i + 16])
                        return self.moveline
                elif dir == 'down':
                    self.moveline.clear()
                    if board[ i - 16].get_name() == " ":
                        MovesBoard().moveLine(dir,board,board[i - 16])
                        self.moveline.append(board[i - 16])
                        return self.moveline
                elif dir == 'right':
                    if board[i + 1].get_name() == " " :
                        self.moveline.clear()
                        if board[i].get_column() != 0:
                            MovesBoard().moveLine(dir,board,board[i + 1])
                            self.moveline.append(board[i + 1])
                            return self.moveline
                elif dir == 'left':
                    if board[i - 1].get_name() == " " :
                        self.moveline.clear()
                        if board[i].get_column() != 0:
                            MovesBoard().moveLine(dir,board,board[i - 1])
                            self.moveline.append(board[i - 1])
                            return self.moveline

    def moveDiagonal(self,dir,board,boardI):
        """

        Resuelve la cantidad de espacio libre entre un pieza origen para poder hacer un movimiento en diagonal de espacio libre

        Devuelve la pieza destino que está situada a una distancia n espacio “ ” antes de otra pieza diferente a  “ ”

        Parámetro
        dir----> Es la dirección donde va resolver
        board----> Tablero del turno
        piece----> pieza origen

        """
        for i in range(0,len(board)):
            if (board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column())and 0<board[i].get_column()<15 and 0<board[i].get_row()<15:
                if dir == 'rd':  # (right diagonal up)
                    self.movediagonal.clear()
                    if board[ i + 17].get_name() == " ":
                            MovesBoard().moveDiagonal(dir,board,board[i + 17])
                            self.movediagonal.append(board[i + 17])
                            return self.movediagonal
                elif dir == 'ldd':  # (left diagonal up)
                    self.movediagonal.clear()
                    if board[i + 15].get_name() == " " :
                            MovesBoard().moveDiagonal(dir,board,board[i + 15])
                            self.movediagonal.append(board[i + 15])
                            return self.movediagonal
                elif dir == 'dr':  # (right diagonal down)
                    self.movediagonal.clear()
                    if board[i - 15].get_name() == " ":
                        MovesBoard().moveDiagonal(dir,board,board[i - 15])
                        self.movediagonal.append(board[i - 15])
                        return self.movediagonal
                elif dir == 'dl':  # (left diagonal down)
                    self.movediagonal.clear()
                    if board[i - 17].get_name() == " " :
                        MovesBoard().moveDiagonal(dir,board,board[i - 17])
                        self.movediagonal.append(board[i - 17])
                        return self.movediagonal

    def moveLineEnemy(self,dir,board,piece,colour):
        """
        Resuelve la cantidad de espacio libre entre un pieza origen para poder hacer un movimiento en línea hasta una pieza enemiga

        Devuelve la pieza destino que es una pieza enemiga

        Parámetro
        dir----> Es la dirección donde va resolver
        board----> Tablero del turno
        piece----> pieza origen
        colour---> Color de pieza a atacar

        """

        for i in range(0,len(board)):
            if (board[i].get_row() == piece.get_row() and board[i].get_column() == piece.get_column()) and 0<board[i].get_column()<15 and 0<board[i].get_row()<15:
                if dir == 'up':
                    self.movelineenemy.clear()
                    if board[i + 16].get_colour() == colour:
                        self.movelineenemy.append(board[i + 16])
                        return self.movelineenemy
                    elif board[i + 16].get_name() == " ":
                        MovesBoard().moveLineEnemy(dir,board,board[i + 16],colour)
                        return self.movelineenemy
                elif dir == 'down':
                    self.movelineenemy.clear()
                    if board[i - 16].get_colour() == colour:
                        self.movelineenemy.append(board[i - 16])
                        return self.movelineenemy
                    elif board[i - 16].get_name() == " ":
                        MovesBoard().moveLineEnemy(dir,board,board[i - 16],colour)
                        return self.movelineenemy
                elif dir == 'right':
                    self.movelineenemy.clear()
                    if board[i + 1].get_colour() == colour :
                        self.movelineenemy.append(board[i + 1])
                        return self.movelineenemy
                    elif board[i + 16].get_name() == " ":
                        MovesBoard().moveLineEnemy(dir,board,board[i + 1],colour)
                        return self.movelineenemy
                elif dir == 'left':
                    self.movelineenemy.clear()
                    if board[i - 1].get_colour() == colour:
                        self.movelineenemy.append(board[i - 1])
                        return self.movelineenemy
                    elif board[i + 16].get_name() == " ":
                        MovesBoard().moveLineEnemy(dir,board,board[i - 1],colour)
                        return self.movelineenemy

    def moveDiagonalEnemy(self,dir,board,piece,colour):
        """
        resuelve la cantidad de espacio libre entre un pieza origen para poder hacer un movimiento en diagonal hasta una pieza enemiga

        devuelve la pieza destino que es una pieza enemiga

        parámetro
        dir----> Es la dirección donde va resolver
        board----> Tablero del turno
        piece----> pieza origen
        colour---> Color de pieza a atacar

        """
        for i in range(0,len(board)):
            if (board[i].get_row() == piece.get_row() and board[i].get_column() == piece.get_column())and 0 <board[i].get_column()<15and 0<board[i].get_row()<15:
                if dir == 'rd':  # (right diagonal up)
                    self.movediagonalenemy.clear()
                    if board[ i + 17].get_colour() == colour :
                            self.movediagonalenemy.append(board[i + 17])
                            return self.movediagonalenemy
                    elif board[ i + 17].get_name() == " ":
                            MovesBoard().moveDiagonalEnemy(dir,board,board[i + 17],colour)
                            return self.movediagonalenemy
                elif dir == 'ldd':  # (left diagonal up
                    self.movediagonalenemy.clear()
                    if board[i + 15].get_colour() == colour :
                            self.movediagonalenemy.append(board[i + 15])
                            return self.movediagonalenemy
                    elif board[i + 15].get_name() == " ":
                            MovesBoard().moveDiagonalEnemy(dir,board,board[i + 15],colour)
                            return self.movediagonalenemy
                elif dir == 'dr':  # (right diagonal down)
                    self.movediagonalenemy.clear()
                    if board[i - 15].get_colour() == colour:
                        self.movediagonalenemy.append(board[i - 15])
                        return self.movediagonalenemy
                    elif board[i - 15].get_name() == " ":
                        MovesBoard().moveDiagonalEnemy(dir,board,board[i - 15],colour)
                        return self.movediagonalenemy
                elif dir == 'dl':  # (left diagonal down
                    self.movediagonalenemy.clear()
                    if board[i - 17].get_colour() == colour :
                        self.movediagonalenemy.append(board[i - 17])
                        return self.movediagonalenemy
                    elif board[i - 17].get_name() == " ":
                        MovesBoard().moveDiagonalEnemy(dir,board,board[i - 17],colour)
                        return self.movediagonalenemy
