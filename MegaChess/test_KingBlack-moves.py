import pytest

from blackStrategy import KingBlack
from board import Board

board = (      'rrhhbbqqkkbbhhrr'
               'rrhhbbbqkkbbhhrr'
               'pppppppppppppppp'
               'pppppppppppppppp'
               'rrrrrrrrrrrrrrrr'
               '                '
               '       k        '
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
boardGame = Board(board).boardGame()
boardGameStart = Board(boardStart).boardGame()
boardGameNone = Board(boardNone).boardGame()

@pytest.mark.parametrize(
   "imput,expected",[
            (boardGameStart,[]),
            (boardGameNone,[]),
            (boardGame,[[6, 7, 7, 7, 30], [6, 7, 5, 7, 30], [6, 7, 6, 8, 30], [6, 7, 6, 6, 30], [6, 7, 5, 6, 30], [6, 7, 7, 8, 30], [6, 7, 5, 8, 30]]
)
       ])
def test_KingBlackMoves(imput,expected):
    assert KingBlack(imput).moves() == expected
