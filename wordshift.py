import random

class game_board:
    """Represents the 3x4 board"""
    def __init__(self):
        self.score = 0
        self.board = ["_"] * 16
        self.dice = [
            "RIFOBX",
            "IFEHEY",
            "DENOWS",
            "UTOKND",
            "HMSRAO",
            "LUPETS",
            "ACITOA",
            "YLGKUE",
            "QBMJOA",
            "EHISPN",
            "VETIGN",
            "BALIYT",
            "EZAVND",
            "RALESC",
            "UWILRG",
            "PACEMD"
        ]

    def print_board(self):
        for i in range(0, len(self.board), 6):
            print("".join(self.board[i:i+6]))

    def shuffle_board(self):
        random.shuffle(self.dice)
        # print(self.dice)
        for i in range(0, len(self.dice)):
            letter = " " + self.dice[i][random.randint(0,5)] + " "
            if letter == " Q ":
                letter = " Qu"
            self.board[i] = letter
        for index in [0, 5, 6, 11, 12, 17, 18, 23]:
            self.board.insert(index, "   ")
        # self.print_board()

    def right_shift(self, row):
        if row == 1:
            if self.board[5] == "   ":
                return "Shift not allowed"
            else:
                self.board.insert(0, "   ")
                self.board.pop(6)
        if row == 2:
            if self.board[11] == "   ":
                return "Shift not allowed"
            else:
                self.board.insert(6, "   ")
                self.board.pop(12)
        if row == 3:
            if self.board[17] == "   ":
                return "Shift not allowed"
            else:
                self.board.insert(12, "   ")
                self.board.pop(18)
        if row == 4:
            if self.board[23] == "   ":
                return "Shift not allowed"
            else:
                self.board.insert(18, "   ")
                self.board.pop(24)
        # self.print_board()

    def left_shift(self, row):
        if row == 1:
            self.board.pop(0)
            self.board.insert(4, "   ")
        if row == 2:
            self.board.pop(6)
            self.board.insert(10, "   ")
        if row == 3:
            self.board.pop(12)
            self.board.insert(16, "   ")
        if row == 4:
            self.board.insert(23, "  ")
            self.board.pop(18)
        # self.print_board()

board_1 = game_board()
board_1.shuffle_board()
board_1.left_shift(2)
board_1.left_shift(4)
board_1.right_shift(1)
print(board_1.right_shift(1))
board_1.print_board()
