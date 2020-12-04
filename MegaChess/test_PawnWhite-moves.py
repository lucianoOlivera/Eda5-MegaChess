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
            (boardGame,[[6, 7, 7, 7, 10]]),
            (boardGameStart,[[3, 0, 4, 0, 10], [3, 0, 5, 0, 10], [3, 1, 4, 1, 10], [3, 1, 5, 1, 10], [3, 2, 4, 2, 10], [3, 2, 5, 2, 10], [3, 3, 4, 3, 10], [3, 3, 5, 3, 10], [3, 4, 4, 4, 10], [3, 4, 5, 4, 10], [3, 5, 4, 5, 10], [3, 5, 5, 5, 10], [3, 6, 4, 6, 10], [3, 6, 5, 6, 10], [3, 7, 4, 7, 10], [3, 7, 5, 7, 10], [3, 8, 4, 8, 10], [3, 8, 5, 8, 10], [3, 9, 4, 9, 10], [3, 9, 5, 9, 10], [3, 10, 4, 10, 10], [3, 10, 5, 10, 10], [3, 11, 4, 11, 10], [3, 11, 5, 11, 10], [3, 12, 4, 12, 10], [3, 12, 5, 12, 10], [3, 13, 4, 13, 10], [3, 13, 5, 13, 10], [3, 14, 4, 14, 10], [3, 14, 5, 14, 10], [3, 15, 4, 15, 10], [3, 15, 5, 15, 10]]),
            (boardGameNone,[])
       ])
def test_PawnBlackMoves(imput,expected):
    assert PawnBlack(imput).moves() == expected
