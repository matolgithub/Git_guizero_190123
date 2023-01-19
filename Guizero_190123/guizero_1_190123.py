from guizero import App, Text, TextBox

app = App(title="My first Guizero application!", bg="grey", width=500, height=300)
message = Text(app, text="It's simple text!", color="red", bg="black", width=20, height=5)
message_box_1 = TextBox(app, text="It is text box!", width=20, height=5, scrollbar=True, align="right")
message_box_2 = TextBox(app, text="It is text box!", width=20, height=5, scrollbar=True, align="left")
message_box_3 = TextBox(app, text="It is text box!", width=20, height=5, scrollbar=True, align="center")
app.display()
