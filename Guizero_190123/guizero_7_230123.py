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

    speed = 1000
    if score > 10:
        speed -= 500
    elif score > 20:
        speed -= 600
    elif score > 30:
        speed -= 700
    elif score > 40:
        speed -= 800

    all_red = True
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if board[x, y].color != "red":
                all_red = False
    if all_red:
        score_display.value = "You lost! Score is: " + str(score)
    else:
        board.after(speed, add_dote)


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
