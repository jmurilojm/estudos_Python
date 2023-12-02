from tkinter import *


app = Tk()


lb = Label(app)
lb['text'] = 'Hello, GUI!'
lb.place(x=100,y=100)

app.title = ('App')
app.geometry('100x100+100+100')
app['background'] = 'yellow'
app.mainloop()