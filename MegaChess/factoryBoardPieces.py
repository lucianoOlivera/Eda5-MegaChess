from core import Bishop,Queen,Empty,Knight,King,Pawn,Rook


class Factory(object):
    def get_BoardPices(self,row,col,name):
        listBoard = []
        if name is "r":
            rook = Rook(row,col,'r')
            listBoard.append(rook)
        elif name is 'h':
            knight = Knight(row,col,'k')
            listBoard.append(knight)
        elif name is 'b':
            bishop = Bishop(row,col,'b')
            listBoard.append(bishop)
        elif name is 'q':
            queen = Queen(row,col,'q')
            listBoard.append(queen)
        elif name is 'k':
            king = King(row,col,'k')
            listBoard.append(king)
        elif name is 'p':
            pawn = Pawn(row,col,'p')
            listBoard.append(pawn)
        elif name is 'R':
            rook = Rook(row,col,'R')
            listBoard.append(rook)
        elif name is 'H':
            knight = Knight(row,col,'H')
            listBoard.append(knight)
        elif name is 'B':
            bishop = Bishop(row,col,'B')
            listBoard.append(bishop)
        elif name is 'Q':
            queen = Queen(row,col,'Q')
            listBoard.append(queen)
        elif name is 'K':
            king = King(row,col,'K')
            listBoard.append(king)
        elif name is 'P':
            pawn = Pawn(row,col,'P')
            listBoard.append(pawn)
        elif name is " ":
            empty = Empty(row,col," ")
            listBoard.append(empty)
        return print(listBoard)
