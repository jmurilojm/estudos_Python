from tkinter import *
from functools import partial


def clique(botao):
    if botao == b1:
        lab1['text'] = 'B1 clicou'
    elif botao == b2:
        lab1['text'] = 'B2 clicou'
    

app = Tk()


b1 = Button(app)
b1['text'] = 'Botão 1'
b1['command'] = partial(clique,b1)
b1.place(x=100,y=100)

b2 = Button(app, text='Botão 2')
b2['command'] = partial(clique,b2)
b2.place(x=100,y=200)


lab1 = Label(app, text='')
lab1.place(x=100,y=300)


app.mainloop()