import pytest

from blackStrategy import QueenBlack
from board import Board


board = (      'rrhhbbqqkkbbhhrr'
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
boardStart = (  'rrhhbbqqkkbbhhrr'
                'rrhhbbbqkkbbhhrr'
                'pppppppppppppppp'
                'pppppppppppppppp'
                '                '
                'PPPPPPPPPPPPPPPP'
                'P              P'
                'P              P'
                'P       q      P'
                'P              P'
                'PPPPPPPPPPPPPPPP'
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
               '      ppp       '
               '      pqp       '
               '      ppp       '
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
            (boardGameStart,[[8, 8, 10, 8, 15], [8, 8, 5, 8, 15], [8, 8, 8, 15, 15], [8, 8, 8, 0, 15], [8, 8, 10, 10, 15], [8, 8, 10, 6, 15], [8, 8, 5, 5, 15], [8, 8, 5, 11, 15]]
)

       ])
def test_QueenBlackMovesAtack(imput,expected):
    assert QueenBlack(imput).movesAtack() == expected
