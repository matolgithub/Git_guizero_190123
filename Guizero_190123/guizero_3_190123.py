import time

from guizero import App, Text, Picture, PushButton
from random import choice


def choose_name():
    print("Button was pressed!")
    first_names = ["Barbara", "Woody", "Jennifer", "Tom", "Rubby"]
    last_names = ["Spindleshanks", "Mysterioso", "Dungeon", "Catseye", "Darkmeyer", "Flamingobreath"]
    text_color = ["white", "black", "green", "yellow", "grey", "pink", "blue", "red"]
    spy_name = choice(first_names) + " " + choice(last_names)
    print(spy_name)
    name.text_color = choice(text_color)
    name.text_size = text_size
    name.value = spy_name


app = App("TOP SECRET")

title = Text(app, "Push the red button to find out your spy name!")
time.sleep(1)
button = PushButton(app, choose_name, text="Tell me!")
button.bg = "red"
button.text_size = 30
button.text_color = "white"
text_size = 20
name = Text(app, text="")

app.display()
