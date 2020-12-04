import pytest

from board import Board
from whiteStrategy import QueenWhite

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
                'pppppppppppppppp'
                'p              p'
                'p              p'
                'p       Q      p'
                'p              p'
                'pppppppppppppppp'
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
               '      PPP       '
               '      PQP       '
               '      PPP       '
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
            (boardGameStart,[[8, 8, 10, 8, 15], [8, 8, 5, 8, 15], [8, 8, 8, 15, 15], [8, 8, 8, 0, 15], [8, 8, 10, 10, 15], [8, 8, 10, 6, 15], [8, 8, 5, 5, 15], [8, 8, 5, 11, 15]])
        ])
def test_QueenWhiteMovesAtack(imput,expected):
    assert QueenWhite(imput).movesAtack() == expected
