from guizero import App, Text, PushButton, info, Waffle
import random

colours = ["red", "blue", "green", "yellow", "magenta", "purple"]
board_size = 14
movies_limit = 25
movies_taken = 0


def flood(x, y, target, replacement):
    if target == replacement:
        return False
    if board.get_pixel(x, y) != target:
        return False
    board.set_pixel(x, y, replacement)
    if y + 1 <= board_size - 1:
        flood(x, y + 1, target, replacement)
    if y - 1 >= 0:
        flood(x, y - 1, target, replacement)
    if x + 1 <= board_size - 1:
        flood(x + 1, y, target, replacement)
    if x - 1 >= 0:
        flood(x - 1, y, target, replacement)


def all_squares_are_the_same():
    squares = board.get_all()
    if all(colour == squares[0] for colour in squares):
        return True
    else:
        return False


def win_check():
    global movies_taken
    movies_taken += 1
    if movies_taken <= movies_limit:
        if all_squares_are_the_same():
            win_text.value = "You win!"
        else:
            win_text.value = "You lost :("


def h11_board():
    for x in range(board_size):
        for y in range(board_size):
            board.set_pixel(x, y, random.choice(colours))


def init_palette():
    for colour in colours:
        palette.set_pixel(colours.index(colour), 0, colour)


def start_flood(x, y):
    flood_colour = palette.get_pixel(x, y)
    target = board.get_pixel(0, 0)
    flood(0, 0, target, flood_colour)
    win_check()


app = App("Flood it")

board = Waffle(app, width=board_size, height=board_size, pad=0)
palette = Waffle(app, width=6, height=1, dotty=True, command=start_flood)
win_text = Text(app)

h11_board()
init_palette()

app.display()
