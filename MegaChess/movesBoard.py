class MovesBoard():
    down = []
    up = []
    right = []
    left = []
    rd = []
    downe = []
    upe = []
    righte = []
    lefte = []
    ldd = []
    dr = []
    dl = []
    rde = []
    ldde = []
    dre = []
    dle = []
    def moveLine(self,dir,board,boardI):
        for i in range(0,len(board)):
            if (board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column()) and 0<board[i].get_column()<15 and 0<board[i].get_row()<15:
                if dir == 'up':
                    self.up.clear()
                    if board[i + 16].get_name() == " ":
                        MovesBoard().moveLine(dir,board,board[i + 16])
                        self.up.append(board[i + 16])
                        return self.up
                elif dir == 'down':
                    self.down.clear()
                    if board[ i - 16].get_name() == " ":
                        MovesBoard().moveLine(dir,board,board[i - 16])
                        self.down.append(board[i - 16])
                        return self.down
                elif dir == 'right':
                    if board[i + 1].get_name() == " " :
                        self.right.clear()
                        if board[i].get_column() != 0:
                            MovesBoard().moveLine(dir,board,board[i + 1])
                            self.right.append(board[i + 1])
                            return self.right
                elif dir == 'left':
                    if board[i - 1].get_name() == " " :
                        self.left.clear()
                        if board[i].get_column() != 0:
                            MovesBoard().moveLine(dir,board,board[i - 1])
                            self.left.append(board[i - 1])
                            return self.left

    def moveDiagonal(self,dir,board,boardI):

        for i in range(0,len(board)):
            if (board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column())and 0<board[i].get_column()<15 and 0<board[i].get_row()<15:
                if dir == 'rd':  # (right diagonal up)
                    self.rd.clear()
                    if board[ i + 17].get_name() == " ":
                            MovesBoard().moveDiagonal(dir,board,board[i + 17])
                            self.rd.append(board[i + 17])
                            return self.rd
                elif dir == 'ldd':  # (left diagonal up)
                    self.ldd.clear()
                    if board[i + 15].get_name() == " " :
                            MovesBoard().moveDiagonal(dir,board,board[i + 15])
                            self.ldd.append(board[i + 15])
                            return self.ldd
                elif dir == 'dr':  # (right diagonal down)
                    self.dr.clear()
                    if board[i - 15].get_name() == " ":
                        MovesBoard().moveDiagonal(dir,board,board[i - 15])
                        self.dr.append(board[i - 15])
                        return self.dr
                elif dir == 'dl':  # (left diagonal down)
                    self.dl.clear()
                    if board[i - 17].get_name() == " " :
                        MovesBoard().moveDiagonal(dir,board,board[i - 17])
                        self.dl.append(board[i - 17])
                        return self.dl

    def moveLineEnemy(self,dir,board,boardI,colour):
        for i in range(0,len(board)):
            if (board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column()) and 0<board[i].get_column()<15 and 0<board[i].get_row()<15:
                if dir == 'up':
                    self.upe.clear()
                    if board[i + 16].get_colour() == colour:
                        self.upe.append(board[i + 16])
                        return self.upe
                    elif board[i + 16].get_name() == " ":
                        MovesBoard().moveLineEnemy(dir,board,board[i + 16],colour)
                        return self.upe
                elif dir == 'down':
                    self.downe.clear()
                    if board[i - 16].get_colour() == colour:
                        self.downe.append(board[i - 16])
                        return self.downe
                    elif board[i - 16].get_name() == " ":
                        MovesBoard().moveLineEnemy(dir,board,board[i - 16],colour)
                        return self.downe
                elif dir == 'right':
                    self.righte.clear()
                    if board[i + 1].get_colour() == colour :
                        self.righte.append(board[i + 1])
                        return self.righte
                    elif board[i + 16].get_name() == " ":
                        MovesBoard().moveLineEnemy(dir,board,board[i + 1],colour)
                        return self.righte
                elif dir == 'left':
                    self.lefte.clear()
                    if board[i - 1].get_colour() == colour:
                        self.lefte.append(board[i - 1])
                        return self.lefte
                    elif board[i + 16].get_name() == " ":
                        MovesBoard().moveLineEnemy(dir,board,board[i - 1],colour)
                        return self.lefte

    def moveDiagonalEnemy(self,dir,board,boardI,colour):
        for i in range(0,len(board)):
            if (board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column())and 0 <board[i].get_column()<15and 0<board[i].get_row()<15:
                if dir == 'rd':  # (right diagonal up)
                    self.rde.clear()
                    if board[ i + 17].get_colour() == colour :
                            self.rde.append(board[i + 17])
                            return self.rde
                    elif board[ i + 17].get_name() == " ":
                            MovesBoard().moveDiagonalEnemy(dir,board,board[i + 17],colour)
                            return self.rde
                elif dir == 'ldd':  # (left diagonal up
                    self.ldde.clear()
                    if board[i + 15].get_colour() == colour :
                            self.ldde.append(board[i + 15])
                            return self.ldde
                    elif board[i + 15].get_name() == " ":
                            MovesBoard().moveDiagonalEnemy(dir,board,board[i + 15],colour)
                            return self.ldde
                elif dir == 'dr':  # (right diagonal down)
                    self.dre.clear()
                    if board[i - 15].get_colour() == colour:
                        self.dre.append(board[i - 15])
                        return self.dre
                    elif board[i - 15].get_name() == " ":
                        MovesBoard().moveDiagonalEnemy(dir,board,board[i - 15],colour)
                        return self.dre
                elif dir == 'dl':  # (left diagonal down
                    self.dle.clear()
                    if board[i - 17].get_colour() == colour :
                        self.dle.append(board[i - 17])
                        return self.dle
                    elif board[i - 17].get_name() == " ":
                        MovesBoard().moveDiagonalEnemy(dir,board,board[i - 17],colour)
                        return self.dle
