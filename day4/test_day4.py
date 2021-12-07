import pytest

from one import BingoBoard


@pytest.fixture
def board():
    board_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return BingoBoard(board_data)


class TestBingoBoard:
    def test_is_winner__horizontal(self, board):
        board.board[0][0] = None
        board.board[0][1] = None
        board.board[0][2] = None

        assert board.is_winner()

    def test_is_winner__vertical(self, board):
        board.board[0][1] = None
        board.board[1][1] = None
        board.board[2][1] = None

        assert board.is_winner()

    def test_mark_number(self, board):
        board.mark_number(8)
        assert board.board[2][1] == None
