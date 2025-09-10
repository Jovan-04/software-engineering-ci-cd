from copy import deepcopy
import time
import os

class Game_Of_Life:
    def __init__(self, size: int = 8) -> None:
        self.board = [[0] * size for _ in range(size)]
        self.size = size

    def set_cell(self, r: int, c: int, state: int):
        self.board[r][c] = state

    def tick(self):
        updated_board = deepcopy(self.board)
        for i in range(self.size):
            for j in range(self.size):
                live_count = self.count_live_neighbors(i, j)
                if live_count < 2:
                    updated_board[i][j] = 0

                elif live_count == 3:
                    updated_board[i][j] = 1

                elif live_count > 3:
                    updated_board[i][j] = 0

        self.board = updated_board

    def count_live_neighbors(self, r: int, c: int) -> int:
        live_count = 0
        for i in range(r-1, r+2):
            for j in range(c-1, c+2):
                if i == r and j == c:
                    continue
                if i >= self.size or i < 0 or j >= self.size or j < 0:
                    continue
                if self.board[i][j] == 1:
                    live_count += 1
        return live_count
    
    def __repr__(self):
        s = ''
        for row in self.board:
            for entry in row:
                if entry == 0:
                    s += '⬜ '
                else:
                    s += '⬛ '
       
            s += '\n'
        return s

    def animate(self, frames = 20, frame_time = 1):
        for _ in range(frames):
            os.system("clear")
            print(self)
            self.tick()
            time.sleep(frame_time)