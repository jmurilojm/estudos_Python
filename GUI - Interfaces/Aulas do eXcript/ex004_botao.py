from tkinter import *


def clique():
    print('botao1 foi clicado')# console
    descricao['text'] = 'Python'


app = Tk()


botao1 = Button(app,width=10, text='Next', command=clique)
botao1.place(x=350,y=1000)

descricao = Label(app, bg= 'yellow',text='Programando em...')
descricao.place(x=350,y=500)


app['bg'] = 'yellow'
app.mainloop()