import typing as T


class BingoBoard:
    def __init__(self, board_data: T.List[T.List[int]]):
        # things are square for now
        self.length = len(board_data[0])
        self.width = len(board_data[0])

        self.board = ["" for _ in range(self.length)]
        for x in range(len(self.board)):
            self.board[x] = ["" for _ in range(self.length)]
        # load data onto the board
        for x in range(self.length):
            for y in range(self.length):
                self.board[x][y] = int(board_data[x][y])

    def __repr__(self):
        pretty_board_data = self.board
        return f"<{__class__.__name__}> {pretty_board_data}"

    def mark_number(self, num: int):
        """All cells a value of num are 'marked'."""
        for x in range(self.length):
            for y in range(self.length):
                if self.board[x][y] == num:
                    self.board[x][y] = None

    def is_winner(self):
        # NOTE: there is definitely a less cringy way to do this
        # winner by row
        for x in range(len(self.board)):
            if all([cell is None for cell in self.board[x]]):
                return True
        # winner by column
        for y in range(self.length):
            col = []
            for x in range(self.length):
                col.append(self.board[x][y])
            if all([cell is None for cell in col]):
                return True
        # not a winner
        return False

    def unmarked_num_sum(self) -> int:
        """returns the sum of all unmarked numbers on the board"""
        total = 0
        for x in range(self.length):
            for y in range(self.length):
                if self.board[x][y]:
                    total += self.board[x][y]

        return total


def main():
    boards = load_boards()
    winning_board = None
    for num in turns():
        if winning_board:
            break
        for board in boards:
            board.mark_number(num)
            if board.is_winner:
                winning_board = board
                winning_called_num = num

    if winning_board:
        print(f"Winning Board: {winning_board}")
        print(f"Last number called: {winning_called_num}")
        print(f"Sum of unmarked numbers: {winning_board.unmarked_num_sum()}")
        print(f"Final Score: {winning_board.unmarked_num_sum() * winning_called_num}")
    else:
        print("No winning board found")


def load_boards() -> T.List[BingoBoard]:
    with open("boards.txt", "r") as f:
        file_data = f.read().split("\n")

    data = []
    boards = []
    for row in file_data:
        # new board data
        if row == "":
            boards.append(BingoBoard(data))
            data = []
        else:
            data.append([int(val) for val in row.split(" ") if val])
    return boards


def turns() -> T.List[str]:
    with open("turns.txt", "r") as f:
        turn_list = [int(turn) for turn in f.read().split(",")]
    return turn_list


if __name__ == "__main__":
    main()
