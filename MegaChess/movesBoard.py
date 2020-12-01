class MovesBoard():
    down = []
    up = []
    right = []
    left = []
    rd = []
    ldd = []
    dr = []
    dl = []

    def moveLine(self,dir,board,boardI):

        for i in range(0,len(board)):
            if dir == 'up':
                if board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column() and board[i + 16].get_name() == " ":
                    MovesBoard().moveLine(dir,board,board[i + 16])
                    self.up.append(board[i + 16])
                    return self.up
            elif dir == 'down':
                if board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column() and board[ i - 16].get_name() == " ":
                    MovesBoard().moveLine(dir,board,board[i - 16])
                    self.down.append(board[i - 16])
                    return self.down
            elif dir == 'right':
                if board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column() and board[i + 1].get_name() == " " and board[i].get_column()<15:
                    if board[i].get_column() != 0:
                        MovesBoard().moveLine(dir,board,board[i + 1])
                        self.right.append(board[i + 1])
                        return self.right
            elif dir == 'left':
                if board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column() and board[i - 1].get_name() == " " and board[i].get_column()>0:
                    if board[i].get_column() != 0:
                        MovesBoard().moveLine(dir,board,board[i - 1])
                        self.left.append(board[i - 1])
                        return self.left

    def moveDiagonal(self,dir,board,boardI):
        for i in range(0,len(board)):
            if dir == 'rd':  # (right diagonal up)
                if (board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column()) and board[ i + 17].get_name() == " " and board[i].get_column()<15:
                    if board[i].get_column() != 0:
                        MovesBoard().moveDiagonal(dir,board,board[i + 17])
                        self.rd.append(board[i + 17])
                        print(self.rd)
                        return self.rd

            elif dir == 'ldd':  # (left diagonal up)
                if board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column() and board[i + 15].get_name() == " " and board[i].get_column()>0:
                    if board[i].get_column() != 15:
                        MovesBoard().moveDiagonal(dir,board,board[i + 15])
                        self.ldd.append(board[i + 15])
                        return self.ldd
            elif dir == 'dr':  # (right diagonal down)
                if board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column() and board[i - 15].get_name() == " " and board[i].get_column()<15:
                    if board[i].get_column() != 0:
                        MovesBoard().moveDiagonal(dir,board,board[i - 15])
                        self.dr.append(board[i - 15])
                        return self.dr
            elif dir == 'dl':  # (left diagonal down)
                if board[i].get_row() == boardI.get_row() and board[i].get_column() == boardI.get_column() and board[i - 17].get_name() == " " and board[i].get_column()>0:
                    if board[i].get_column() != 15:
                        MovesBoard().moveDiagonal(dir,board,board[i - 17])
                        self.dl.append(board[i - 17])
                        return self.dl
