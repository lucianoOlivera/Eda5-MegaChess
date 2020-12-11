import pytest
from piecesStrategy import MoveScore
from factoryBoardPieces import FactoryBoardPieces

piecePawn = FactoryBoardPieces().get_BoardPieces(5,0,"p")
pieceKnight = FactoryBoardPieces().get_BoardPieces(3,5,"H")
pieceRook = FactoryBoardPieces().get_BoardPieces(3,1,"r")
pieceBishop = FactoryBoardPieces().get_BoardPieces(6,3,"b")
pieceQueen = FactoryBoardPieces().get_BoardPieces(5,0,"Q")

@pytest.mark.parametrize(
    "imput1,imput2,expected",[
        (piecePawn," ",10),
        (pieceKnight,"p",40),
        (pieceRook,"k",160),
        (pieceBishop," ",40),
        (pieceQueen,"q",60)
        ])
def test_MovesScore(imput1,imput2,expected):
    assert MoveScore().moveScore(imput1,imput2) == expected
