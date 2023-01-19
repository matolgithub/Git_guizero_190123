from guizero import App, Text, Picture

app = App("Wanted!")
app.bg = "#FBFBD0"

wanted_text = Text(app, "WANTED")
wanted_text.text_size = 50
wanted_text.text_color = "green"
wanted_text.font = "Times New Roman"

bears = Picture(app, image="pictures/111.png", width=400, height=400)

app.display()
