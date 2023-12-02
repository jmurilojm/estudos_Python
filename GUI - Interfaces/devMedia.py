from tkinter import *

class App:
    def __init__(self,  master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()


        self.msg = Label(self.widget1, text='Primeiro widget')
        self.msg['font'] = ('Verdana','10','italic','bold')
        self.msg.pack()

        self.sair = Button(self.widget1)
        self.sair['text'] = 'Sair'
        self.sair['font'] = ('Calibri','10')
        self.sair['width'] = 20
        #self.sair['command'] = self.widget1.quit
        #self.sair.bind('<Button-1>',self.mudarTexto)
        self.sair['command'] = self.mudarTexto
        self.sair.pack()

    #def mudarTexto(self, event):
    def mudarTexto(self):
        if self.msg['text'] == 'Primeiro widget':
            self.msg['text'] = 'O botao recebeu um clique'
        else:
            self.msg['text'] = 'Primeiro widget. Fim!'
            self.sair['command'] = self.widget1.quit
        pass


root = Tk()
App(root)
root.mainloop()