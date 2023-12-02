from tkinter import *

class Aplicativo:
    def __init__(self,nome):
        #Frames
        self.frame = Frame(nome)
        self.frame.pack(fill='both',pady=50)
        
        self.frame1 = Frame(nome)
        self.frame1.pack(fill='both',padx=50,pady=50)
        self.frame2 = Frame(nome)
        self.frame2.pack(fill='both',padx=50,pady=50)
        self.frame3 = Frame(nome)
        self.frame3.pack(fill='both',padx=50,pady=50)
        
        #Itens do frame
        self.label = Label(self.frame,text='ÁREA - Retângulos e Quadrados')
        self.label.pack()
        
        #Itens do frame1
        self.label1 = Label(self.frame1,text='Base')
        self.label1.pack(side='left')
        self.base = Entry(self.frame1,width=30)
        self.base.pack(side='right')
        
        #Itens do frame2
        self.label2 = Label(self.frame2,text='Altura')
        self.label2.pack(side='left')
        self.altura = Entry(self.frame2,width=30)
        self.altura.pack(side='right')
        
        #Itens do frame3
        self.butao = Button(self.frame3,text='Calcular',command=self.logar)
        self.butao.pack()
        self.label3 = Label(self.frame3,text='',bg='white',width=20)
        self.label3.pack(side='bottom',pady=50)
        
        
    def logar(self):
        base = int(self.base.get())
        altura = int(self.altura.get())
        
        calculo = base * altura
        
        self.label3['text'] = f'Área = {calculo}'
        
        
janela = Tk()


app = Aplicativo(janela)


janela.mainloop()