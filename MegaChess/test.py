import unittest

from board import Board
from game import Game


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = "rrhhbbqqkkbbhhrrrrhhbbbqkkbbhhrrpppppppppppppppppppppppppppppppp                    q                                                                                                   P       PPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"
        self.a = Game(12,"black",23)
        self.b = "[3, 0, 4, 0, 10]"

    def test_Board(self):
        self.assertEqual(self.a.defineStrategy(self.board),self.b,"Is not Equals")
