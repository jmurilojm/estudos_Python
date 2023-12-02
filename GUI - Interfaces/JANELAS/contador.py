from tkinter import *

class App:
    def __init__(self):
        
        janela = Tk()
        
        titulo = Label(janela,text='TOTAL DE CARACTERES EM UM TEXTO')
        titulo.pack(pady=50)
        
        self.texto = Entry(janela,bd=5)
        self.texto.pack(pady=200)
        
        butao = Button(janela,bd=3,text='ANALIZAR',command=self.analizar)
        butao.pack()
        
        subtitulo = Label(janela,text='Resultado da analise:')
        subtitulo.pack(pady=200)
        
        self.resultado = Label(janela,text='',justify=LEFT)
        self.resultado.pack()
        
        
        
        janela.mainloop()
        
        
    def analizar(self):
        digitacao = self.texto.get().upper()
        
        vogal = ['A','Á','Â','Ã''À',
        'E','É','Ê','È',
        'I','Í','Ì',
        'O','Ó','Ô','Õ','Ò',
        'U','Ú']
        
        especial = ['.',',',':',';','?','!',"'",'"','-','_','(',')','=','/','$','#','@','*','+','&','%']
        
        total = 0
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
                
            
        self.resultado['text'] = f'Total de digitos..............: {total}\nTotal de caracteres........: {caracteres}\nTotal de consoantes......: {consoantes}\nTotal de vogais..............: {vogais}\nTotal de espaços...........: {espacos}\nTotal de números...........: {numeros}\nTotal de especiais..........: {especiais}'
        pass
            
        
        
App()