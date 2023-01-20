from guizero import App, Text, Slider, Combo, PushButton
from time import ctime
from string import ascii_letters


def flash_text():
    if title.visible:
        title.hide()
    else:
        title.show()


def update_date():
    the_date.value = ctime((date_slider.value))
    the_date.text_color = "white"
    the_date.size = 20


def are_you_sure():
    if app.yesno("Confirmation", "Are you sure?"):
        app.info("Thanks", "Button pressed")
    else:
        app.error("Ok", "Cancelling")


app = App("Its all gone wrong", bg="dark green")

the_date = Text(app)
date_slider = Slider(app, start=0, end=9999999999, command=update_date)

line = Text(app, "<---------------------------------------------------->", bg="red")
name_letters = []
for count in range(10):
    a_letter = Combo(app, options=" " + ascii_letters, align="top")
    a_letter.text_color = "white"
    a_letter.text_size = 10
    name_letters.append(a_letter)

line = Text(app, "<---------------------------------------------------->", bg="red")

button = PushButton(app, command=are_you_sure)
app.info("Aplication started", "Well done you started the application")

line = Text(app, "<---------------------------------------------------->", bg="red")
title = Text(app, text="Hard to read", size=14, font="Comic Sans", color="green")
app.repeat(1000, flash_text)

app.display()
