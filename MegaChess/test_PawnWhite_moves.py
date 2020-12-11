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
            (boardGameStart,[[12, 0, 11, 0, 15], [12, 1, 11, 1, 15], [12, 2, 11, 2, 15], [12, 3, 11, 3, 15], [12, 4, 11, 4, 15], [12, 5, 11, 5, 15], [12, 6, 11, 6, 15], [12, 7, 11, 7, 15], [12, 8, 11, 8, 15], [12, 9, 11, 9, 15], [12, 10, 11, 10, 15], [12, 11, 11, 11, 15], [12, 12, 11, 12, 15], [12, 13, 11, 13, 15], [12, 14, 11, 14, 15], [12, 15, 11, 15, 15]]),
            (boardGame,[[9, 6, 8, 6, 15]])
       ])
def test_PawnWhiteMoves(imput,expected):
    assert PawnWhite(imput).moves() == expected
