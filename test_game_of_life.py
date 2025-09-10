# Rules

# 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

from game_of_life import Game_Of_Life


def test_init_game():
    game = Game_Of_Life()
    assert game, "no game object :("

def test_init_board():
    game = Game_Of_Life(8)
    assert game.board == [[0] * 8 for _ in range(8)]

def test_board_size_attribute():
    game = Game_Of_Life(8)
    assert game.size == 8

def test_populate_board():
    game = Game_Of_Life(3)
    game.set_cell(0, 0, 1)
    assert game.board == [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

def test_underpopulation_friendless():
    game = Game_Of_Life(3)
    game.set_cell(1, 1, 1)
    game.tick()
    assert game.board == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def test_underpopulation_with_friend():
    game = Game_Of_Life(3)
    game.set_cell(1, 1, 1)
    game.set_cell(2, 2, 1)
    game.tick()
    assert game.board == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def test_many_friends():
    game = Game_Of_Life(3)
    game.board = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    game.tick()
    assert game.board == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

def test_too_many_friends():
    game = Game_Of_Life(3)
    game.board = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    game.tick()
    assert game.board == [[0, 1, 0], [1, 0, 1], [0, 1, 0]]

def test_just_enough_friends():
    game = Game_Of_Life(3)
    game.board = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    game.tick()
    assert game.board == [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
