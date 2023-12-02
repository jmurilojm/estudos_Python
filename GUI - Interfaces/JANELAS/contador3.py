from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self):
        
        janela = Tk()
        
        titulo = Label(janela,text='TOTAL DE CARACTERES EM UM TEXTO')
        titulo.pack(pady=50)
        
        self.tela = Text(janela)
        self.tela.pack()
        
        butao = Button(janela,bd=3,text='ANALIZAR',command=self.analizar)
        butao.pack(pady=30)
        
        self.resultado = Label(janela,text='',justify=LEFT)
        self.resultado.pack()
        
        
        
        janela.mainloop()
        
        
    def analizar(self):
        digitacao = self.tela.get('1.0',END).upper()
        
        vogal = ['A','Á','Â','Ã''À',
        'E','É','Ê','È',
        'I','Í','Ì',
        'O','Ó','Ô','Õ','Ò',
        'U','Ú']
        
        especial = ['.',',',':',';','?','!',"'",'"','-','_','(',')','=','/','$','#','@','*','+','&','%']
        
        total = -1
        caracteres = 0
        consoantes = 0
        vogais = 0
        espacos = 0
        numeros = 0
        especiais = 0
        
        for digito in digitacao:
            total += 1
            
            if digito in vogal:
                vogais += 1
                
            if digito == ' ':
                espacos += 1
                
            if digito.isdigit() == True:
                numeros += 1
                
            if digito in especial:
                especiais += 1
                
            caracteres = total - espacos
            consoantes = total - (vogais+espacos+numeros+especiais)
                
                
        messagebox.showinfo('Resultado',f'Total de digitos..............: {total}\nTotal de caracteres........: {caracteres}\nTotal de consoantes......: {consoantes}\nTotal de vogais..............: {vogais}\nTotal de espaços...........: {espacos}\nTotal de números...........: {numeros}\nTotal de especiais..........: {especiais}')
        pass
            
        
        
App()