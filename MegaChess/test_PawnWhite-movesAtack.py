import pytest

from board import Board
from whiteStrategy import PawnWhite

board = (      'rrhhbbqqkkbbhhrr'
               'rrhhbbbqkkbbhhrr'
               'pppppppppppppppp'
               'pppppppppppppppp'
               '                '
               '                '
               '                '
               '                '
               '     ppp        '
               '      P         '
               '                '
               'RRRRRRRRRRRRRRRR'
               'PPPPPPPPPPPPPPPP'
               'PPPPPPPPPPPPPPPP'
               'RRHHBBQQKKBBHHRR'
               'RRHHBBQQKKBBHHRR')
boardStart = (  'rrhhbbqqkkbbhhrr'
                'rrhhbbbqkkbbhhrr'
                'pppppppppppppppp'
                'pppppppppppppppp'
                '                '
                '                '
                '                '
                '                '
                '                '
                '                '
                '                '
                '                '
                'PPPPPPPPPPPPPPPP'
                'PPPPPPPPPPPPPPPP'
                'RRHHBBQQKKBBHHRR'
                'RRHHBBQQKKBBHHRR')

boardNone=  (  'rrhhbbqqkkbbhhrr'
               'rrhhbbbqkkbbhhrr'
               'pppppppppppppppp'
               'pppppppppppppppp'
               'rrrrrrrrrrrrrrrr'
               '                '
               '                '
               '                '
               '                '
               '                '
               '                '
               'RRRRRRRRRRRRRRRR'
               'PPPPPPPPPPPPPPPP'
               'PPPPPPPPPPPPPPPP'
               'RRHHBBQQKKBBHHRR'
               'RRHHBBQQKKBBHHRR')
boardGame = Board(board).boardGame()
boardGameStart = Board(boardStart).boardGame()
boardGameNone = Board(boardNone).boardGame()

@pytest.mark.parametrize(
   "imput,expected",[
            (boardGameNone,[]),
            (boardGameStart,[]),
            (boardGame,[[9, 6, 10, 7, 20], [9, 6, 10, 5, 20]]
)
       ])
def test_PawnWhiteMovesAtack(imput,expected):
    assert PawnWhite(imput).movesAtack() == expected
