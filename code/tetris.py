import os
import random
import time
from threading import Thread

class TetrisGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.current_piece = None

    def display_board(self):
        os.system('clear' if os.name == 'posix' else 'cls')  # Clear the console

        for row in self.board:
            print(' '.join(row))
        print('-' * (self.width * 2 + 1))

    def generate_random_piece(self):
        pieces = [
            [['#', '#', '#', '#']],
            [['#', '#'], ['#', '#']],
            [['#', '#', '#'], ['#', ' ', ' ']],
            [['#', '#', '#'], [' ', ' ', '#']],
            [['#', '#', '#'], ['#', ' ', ' ']],
        ]

        return random.choice(pieces)

    def place_piece(self, piece, row, col):
        for i in range(len(piece)):
            for j in range(len(piece[i])):
                if piece[i][j] == '#':
                    self.board[row + i][col + j] = '#'

    def clear_board(self):
        self.board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def move_down(self):
        if self.current_piece:
            row, col = self.current_piece['position']
            self.clear_board()
            if row < self.height - len(self.current_piece['shape']):
                self.place_piece(self.current_piece['shape'], row + 1, col)
                self.current_piece['position'] = (row + 1, col)
            else:
                self.current_piece = None
                self.clear_lines()

    def move_left(self):
        if self.current_piece:
            row, col = self.current_piece['position']
            self.clear_board()
            if col > 0:
                self.place_piece(self.current_piece['shape'], row, col - 1)
                self.current_piece['position'] = (row, col - 1)

    def move_right(self):
        if self.current_piece:
            row, col = self.current_piece['position']
            self.clear_board()
            if col < self.width - len(self.current_piece['shape'][0]):
                self.place_piece(self.current_piece['shape'], row, col + 1)
                self.current_piece['position'] = (row, col + 1)

    def rotate_piece(self):
        if self.current_piece:
            row, col = self.current_piece['position']
            rotated_piece = list(zip(*reversed(self.current_piece['shape'])))
            self.clear_board()
            if col <= self.width - len(rotated_piece[0]) and row <= self.height - len(rotated_piece):
                self.place_piece(rotated_piece, row, col)
                self.current_piece['shape'] = rotated_piece

    def clear_lines(self):
        for i in range(self.height - 1, 0, -1):
            if ' ' not in self.board[i]:
                del self.board[i]
                self.board.insert(0, [' ' for _ in range(self.width)])

    def start_game(self):
        self.current_piece = {'shape': self.generate_random_piece(), 'position': (0, self.width // 2 - 1)}

        while True:
            self.move_down()
            self.display_board()
            time.sleep(0.5)

if __name__ == "__main__":
    tetris = TetrisGame(width=10, height=20)

    # Create a separate thread to run the game loop
    game_thread = Thread(target=tetris.start_game)
    game_thread.start()

    # Main thread for handling user input
    while True:
        user_input = input("Enter a command (a: left, d: right, s: down, r: rotate, q: quit): ").lower()

        if user_input == 'a':
            tetris.move_left()
        elif user_input == 'd':
            tetris.move_right()
        elif user_input == 's':
            tetris.move_down()
        elif user_input == 'r':
            tetris.rotate_piece()
        elif user_input == 'q':
            break

    # Wait for the game thread to finish
    game_thread.join()
