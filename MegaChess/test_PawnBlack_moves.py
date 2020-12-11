import pytest

from blackStrategy import PawnBlack
from board import Board

board = (      'rrhhbbqqkkbbhhrr'
               'rrhhbbbqkkbbhhrr'
               'pppppppppppppppp'
               'pppppppppppppppp'
               'rrrrrrrrrrrrrrrr'
               '                '
               '       p        '
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
            (boardGame,[[6, 7, 7, 7, 16]]),
            (boardGameStart,[[3, 0, 5, 0, 15], [3, 1, 5, 1, 15], [3, 2, 5, 2, 15], [3, 3, 5, 3, 15], [3, 4, 5, 4, 15], [3, 5, 5, 5, 15], [3, 6, 5, 6, 15], [3, 7, 5, 7, 15], [3, 8, 5, 8, 15], [3, 9, 5, 9, 15], [3, 10, 5, 10, 15], [3, 11, 5, 11, 15], [3, 12, 5, 12, 15], [3, 13, 5, 13, 15], [3, 14, 5, 14, 15], [3, 15, 5, 15, 15]]
),
            (boardGameNone,[])
       ])
def test_PawnBlackMoves(imput,expected):
    assert PawnBlack(imput).moves() == expected
