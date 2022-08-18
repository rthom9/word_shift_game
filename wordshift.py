import random
import enchant
import time
import sys

dictionary = enchant.Dict("en_US")

class GameBoard:
    """Represents the 3x4 board"""
    def __init__(self):
        self.score = 0
        self.board = ["_"] * 16
        self.word = ""
        self.word_list = []
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
            "A": 1,
            "B": 3,
            "C": 3,
            "D": 2,
            "E": 1,
            "F": 4,
            "G": 2,
            "H": 4,
            "I": 1,
            "J": 8,
            "K": 5,
            "L": 1,
            "M": 3,
            "N": 1,
            "O": 1,
            "P": 3,
            "Q": 10,
            "R": 1,
            "S": 1,
            "T": 1,
            "U": 1,
            "V": 4,
            "W": 4,
            "X": 8,
            "Y": 4,
            "Z": 10,
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
            self.word += self.board[index_selected].strip()
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
                self.word += self.board[index_selected].strip()
                # Update last index
                self.last_index = index_selected
                # Add index selected to list, future checks if letter selected twice
                self.letter_indexes.append(index_selected)

    def backspace(self):
        """With event listener for backspace key"""
        if len(self.word) > 0:
            self.word = self.word[:-1]
        else:
            return

    def word_check(self):
        """With event listener for enter key or enter button
        Checks if current word_string is present in dictionary
        If word not valid, returns invalid message, clears word variable and indexes
        If word is valid, adds to word list, scores word, adds to score total, clears word variable and indexes"""
        # score word
        if dictionary.check(self.word):
            word_score = 0
            # Add up letter values in word, will account for Qu scoring
            for letter in self.word:
                word_score += self.letter_values[letter]
            # If word is 5 letters long (10)
            if len(self.word) >= 5:
                word_score += 10
            # If word is 6 letters long (20)
            if len(self.word) >= 6:
                word_score += 20
            # If word is 7 letters long (30 points)
            if len(self.word) >= 7:
                word_score += 40
            # Add word to word list
            self.word_list.append(self.word)
            self.score += word_score
            self.word = ""
            self.last_index = None
        else:
            self.word = ""
            self.last_index = None
            return "Not a word!"

    def timer(self):
        """Starts with game beginning, when ends, gives total score, adds total score to player's dictionary,
        increments player's games played"""
        game_time = 10
        while game_time:
            mins, secs = divmod(game_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            sys.stdout.flush()
            time.sleep(1)
            game_time -= 1
        print("End Game!")


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
board_1.word_string(3)
board_1.word_string(9)
board_1.word_string(14)
board_1.word_string(15)
board_1.word_string(22)
print(board_1.word_string(9))
print(board_1.word)
board_1.backspace()
print(board_1.word)
print(board_1.word_check())
print(dictionary.check("hello"))
board_1.timer()
