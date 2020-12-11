import pytest

from board import Board
from blackStrategy import KnightBlack

board = (      'rrhhbbqqkkbbhhrr'
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
               '                '
               'PPPPPPPPPPPPPPPP'
               'PPPPPPPPPPPPPPPP'
               'RRHHBBQQKKBBHHRR'
               'RRHHBBQQKKBBHHRR')
boardStart = (  'rrhhbbqqkkbbhhrr'
                'rrhhbbbqkkbbhhrr'
                'pppppppppppppppp'
                'pppppppppppppppp'
                '                '
                '  PPPPPPPPPPP   '
                '  PPPPPPPPPPP   '
                '      php       '
                '  PPPPPPPPPPP   '
                '  PPPPPPPPPPP   '
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
               '                '
               '                '
               '                '
               '                '
               '        h       '
               '                '
               '                '
               '                '
               'PPPPPPPPPPPPPPPP'
               'PPPPPPPPPPPPPPPP'
               'RRHHBBQQKKBBHHRR'
               'RRHHBBQQKKBBHHRR')
boardGame = Board(board).boardGame()
boardGameStart = Board(boardStart).boardGame()
boardGameNone = Board(boardNone).boardGame()

@pytest.mark.parametrize(
   "imput,expected",[
            (boardGame,[]),
            (boardGameNone,[]),
            (boardGameStart,[[7, 7, 8, 5, 40], [7, 7, 8, 9, 40], [7, 7, 9, 6, 40], [7, 7, 9, 8, 40], [7, 7, 6, 9, 40], [7, 7, 6, 5, 40], [7, 7, 5, 8, 40], [7, 7, 5, 6, 40]]
)
       ])
def test_KnightBlack_MovesAtack(imput,expected):
    assert KnightBlack(imput).movesAtack() == expected
