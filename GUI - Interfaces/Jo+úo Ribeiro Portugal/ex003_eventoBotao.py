from tkinter import *

app = Tk()

def mensagem(x):
    lab = Label(app, text=x)
    lab.pack()

#botao
b1 = Button(app, text='Executar', command=lambda: mensagem('b1'))
b1.pack()

b2 = Button(app, text='Executar', command=lambda: mensagem('b2'))
b2.pack()


app.mainloop()