from pieces import Bishop,Queen,Empty,Knight,King,Pawn,Rook


class Factory(object):
    def get_BoardPices(self,row,col,name):
        if name == "r":
            return Rook(row,col,'r','black')
        elif name == 'h':
            return Knight(row,col,'k','black')
        elif name == 'b':
            return Bishop(row,col,'b','black')
        elif name == 'q':
            return Queen(row,col,'q','black')
        elif name == 'k':
            return King(row,col,'k','black')
        elif name == 'p':
            return Pawn(row,col,'p','black')
        elif name == 'R':
            return Rook(row,col,'R','white')
        elif name == 'H':
            return Knight(row,col,'H','white')
        elif name == 'B':
            return Bishop(row,col,'B','white')
        elif name == 'Q':
            return Queen(row,col,'Q','white')
        elif name == 'K':
            return King(row,col,'K','white')
        elif name == 'P':
            return Pawn(row,col,'P','white')
        elif name == " ":
            return Empty(row,col," ",None)
