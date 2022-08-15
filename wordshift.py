import random


class GameBoard:
    """Represents the 3x4 board"""
    def __init__(self):
        self.score = 0
        self.board = ["_"] * 16
        self.word = ""
        self.last_index = None
        self.letter_indexes = []
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
        self.letter_values = {

        }

    def print_board(self):
        for i in range(0, len(self.board), 6):
            print("".join(self.board[i:i+6]))

    def shuffle_board(self):
        random.shuffle(self.dice)
        # print(self.dice)
        for i in range(0, len(self.dice)):
            letter = " " + self.dice[i][random.randint(0, 5)] + " "
            if letter == " Q ":
                letter = " Qu"
            self.board[i] = letter
        for index in [0, 5, 6, 11, 12, 17, 18, 23]:
            self.board.insert(index, "   ")
        # self.print_board()

    def right_shift(self, row):
        if row == 1:
            if self.board[5] != "   ":
                return "Shift not allowed"
            else:
                self.board.insert(0, "   ")
                self.board.pop(6)
        if row == 2:
            if self.board[11] != "   ":
                return "Shift not allowed"
            else:
                self.board.insert(6, "   ")
                self.board.pop(12)
        if row == 3:
            if self.board[17] != "   ":
                return "Shift not allowed"
            else:
                self.board.insert(12, "   ")
                self.board.pop(18)
        if row == 4:
            if self.board[23] != "   ":
                return "Shift not allowed"
            else:
                self.board.insert(18, "   ")
                self.board.pop(24)
        # self.print_board()

    def left_shift(self, row):
        if row == 1:
            if self.board[0] != "   ":
                return "Shift not allowed"
            else:
                self.board.pop(0)
                self.board.insert(5, "   ")
        if row == 2:
            if self.board[6] != "   ":
                return "Shift not allowed"
            else:
                self.board.pop(6)
                self.board.insert(10, "   ")
        if row == 3:
            if self.board[12] != "   ":
                return "Shift not allowed"
            else:
                self.board.pop(12)
                self.board.insert(16, "   ")
        if row == 4:
            if self.board[23] != "   ":
                return "Shift not allowed"
            else:
                self.board.insert(23, "  ")
                self.board.pop(18)

    def word_string(self, index_selected):
        """Generates string based on player's letter selections.
        Cannot select same letter twice
        Can only select letters in immediate proximity
        Cannot select empty space"""
        # If letter is first one selected
        if self.last_index is None:
            self.word += self.board[index_selected]
            self.last_index = index_selected
        else:
            allowed_indexes = [self.last_index + 1, self.last_index - 1, self.last_index + 5, self.last_index + 6,
                self.last_index + 7, self.last_index - 5, self.last_index - 6, self.last_index - 7]
            if index_selected in self.letter_indexes:
                return "Can't select same letter twice"
             # If user clicking on one of the blank spaces
            elif self.board[index_selected] == "   ":
                return "Can't select blank space"
            elif index_selected not in allowed_indexes:
                return "Selection not allowed"
            else:
                self.word += self.board[index_selected]
                self.last_index = index_selected
                self.letter_indexes.append(index_selected)

    def word_check(self, word):
        """Checks if word is present in dictionary
        If word not valid, returns invalid message, clears word variable and indexes
        If word is valid, adds to word list, clears word variable and indexes"""


class Player:
    """Complete"""
    def __init__(self, name):
        self._name = name
        self._scores = {}
        self._games_played = 0

    def get_name(self):
        """Returns player's name"""
        return self._name

    def get_scores(self):
        """Returns dictionary of player's scores"""
        return self._scores

    def get_games_played(self):
        """Returns number of games player has played"""
        return self._games_played

    def set_games_played(self):
        """Updates number of games played by player by 1"""
        self._games_played = self._games_played + 1

    def set_scores(self, game_number, game_score):
        """Updates dictionary of player's scores"""
        self._scores[game_number] = game_score


board_1 = GameBoard()
board_1.shuffle_board()
board_1.right_shift(1)
board_1.left_shift(1)
board_1.left_shift(1)
board_1.print_board()
board_1.word_string(2)
board_1.word_string(3)
board_1.word_string(8)
board_1.word_string(9)
board_1.word_string(14)
print(board_1.word_string(9))
print(board_1.word)
