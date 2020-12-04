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
               '     p p        '
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
            (boardGameStart,[[12, 0, 11, 0, 10], [12, 1, 11, 1, 10], [12, 2, 11, 2, 10], [12, 3, 11, 3, 10], [12, 4, 11, 4, 10], [12, 5, 11, 5, 10], [12, 6, 11, 6, 10], [12, 7, 11, 7, 10], [12, 8, 11, 8, 10], [12, 9, 11, 9, 10], [12, 10, 11, 10, 10], [12, 11, 11, 11, 10], [12, 12, 11, 12, 10], [12, 13, 11, 13, 10], [12, 14, 11, 14, 10], [12, 15, 11, 15, 10]]),
            (boardGame,[[9, 6, 8, 6, 10]])
       ])
def test_PawnBlackMoves(imput,expected):
    assert PawnWhite(imput).moves() == expected
