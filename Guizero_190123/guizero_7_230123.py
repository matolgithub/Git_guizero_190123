from guizero import App, Text, Waffle
from random import randint

GRID_SIZE = 5
score = 0


def add_dote():
    x, y = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
    while board[x, y].dotty == True:
        x, y = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
    board[x, y].dotty = True
    board.set_pixel(x, y, "red")
    board.after(1000, add_dote)


def destroy_dot(x, y):
    global score
    if board[x, y].dotty == True:
        board[x, y].dotty = False
        board.set_pixel(x, y, "white")
        score += 1
        score_display.value = "Your score is: " + str(score)


app = App("Destroy the dots")
instructions = Text(app, text="Click the dots to destroy them!")
board = Waffle(app, height=GRID_SIZE, width=GRID_SIZE, command=destroy_dot)
board.after(1000, add_dote)
score_display = Text(app, text="Your score is: " + str(score))

app.display()
