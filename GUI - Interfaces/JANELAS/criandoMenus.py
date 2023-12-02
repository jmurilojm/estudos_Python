from tkinter import *
from tkinter import messagebox


def cont():
    exec(open('./contador3.py').read())

app = Tk()


# Criando um Menu
frameMenu = Menu(app)

butOp = Menu(frameMenu,tearoff=0)
butOp.add_command(label='Opção 1',command=cont)
butOp.add_command(label='Opção 2')
butOp.add_command(label='Opção 3')
butOp.add_separator()
butOp.add_command(label='sair',command=app.quit)
frameMenu.add_cascade(label='Nome do Menu',menu=butOp)

butOp2 = Menu(frameMenu)
butOp2.add_command(label='Outras opções')
frameMenu.add_cascade(label='Ferramentas',menu=butOp2)

butOp3 = Menu(frameMenu)
butOp3.add_command(label='Ajuda')
frameMenu.add_cascade(label='Sobre',menu=butOp3)



app.config(menu=frameMenu)

app.mainloop()