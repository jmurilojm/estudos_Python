from tkinter import *

class Aplicativo:
    def __init__(self):
        
        #Criando a Janela
        janela = Tk()
        
        #Frames
        self.frame1 = Frame(janela)
        self.frame1.pack(fill='both',padx=50,pady=50)
        self.frame2 = Frame(janela)
        self.frame2.pack(fill='both',padx=50,pady=50)
        self.frame3 = Frame(janela)
        self.frame3.pack(fill='both',padx=50,pady=50)
        
        #Itens do frame1
        self.label = Label(self.frame1,text='Usuário')
        self.label.pack(side='left')
        self.usuario = Entry(self.frame1,width=30)
        self.usuario.pack(side='right')
        
        #Itens do frame2
        self.label2 = Label(self.frame2,text='Senha')
        self.label2.pack(side='left')
        self.senha = Entry(self.frame2,width=30,show='*')
        self.senha.pack(side='right')
        
        #Itens do frame3
        self.butao = Button(self.frame3,text='logar',command=self.logar)
        self.butao.pack(side='right')
        self.label3 = Label(self.frame3,text='')
        self.label3.pack(side='left')
        
        janela.mainloop()
        
        
    def logar(self):
        usuario = self.usuario.get()
        senha = int(self.senha.get())
        
        if usuario == 'Python' and senha == 3:
            self.label3['text'] = 'Acessando...'
        else:
            self.label3['text'] = 'Negado!'
        
        


Aplicativo()