from tkinter import *
from tkinter import messagebox



top = Tk()
top.geometry("100x100")


def helloCallBack():
    msn = messagebox.showinfo( "Janela Python", "Seja bem vindo(a)!")
 
 
B = Button(top, text ="Clique aqui!", command = helloCallBack)
B.pack(pady=500)



top.mainloop()