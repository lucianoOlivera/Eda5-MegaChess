import unittest

from board import Board


class TestBoard(unittest.TestCase):
    board = ""
    boardTest = ""

    def setUp(self):
        self.board = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                     " \
                "                                                                                   P       PPPPPPPP " \
                "PPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR "
        self.boardTest="rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                        P       PPPPPPPP PPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"

    def test_Board(self):

        self.assertEqual(Board(self.board),self.boardTest,"is not equals")
