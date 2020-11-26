from pieces import Bishop,Queen,Empty,Knight,King,Pawn,Rook


class Factory(object):

    def get_BoardPices(self,row,col,name):
        if name == "r":
            return Rook(row,col,'r')
        elif name == 'h':
            return Knight(row,col,'k')
        elif name == 'b':
            return Bishop(row,col,'b')
        elif name == 'q':
            return Queen(row,col,'q')
        elif name == 'k':
            return King(row,col,'k')
        elif name =='p':
            return Pawn(row,col,'p')
        elif name =='R':
            return Rook(row,col,'R')
        elif name == 'H':
            return Knight(row,col,'H')
        elif name == 'B':
            return Bishop(row,col,'B')
        elif name == 'Q':
            return Queen(row,col,'Q')
        elif name == 'K':
            return King(row,col,'K')
        elif name == 'P':
            return Pawn(row,col,'P')
        elif name == " ":
            return Empty(row,col," ")

