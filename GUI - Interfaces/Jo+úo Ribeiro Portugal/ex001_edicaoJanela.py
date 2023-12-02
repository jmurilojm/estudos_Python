from tkinter import *

app = Tk()

#Titulo
app.title('Programa')

#Tamanho da janela + Onde aparecer
app.geometry('100x100+250+250')

#Redimencionamento
app.resizable(width = True, height = True)

#Tamanho minimo
app.minsize(width = 250, height = 250)

#Tamnho maximo
app.maxsize(width = 450, height = 450)

#Abrir maximizado
app.state('zoomed')

#Abrir minimizado
app.state('iconic')

#Colocar icone da janela
app.iconbitmap('_imag/icone.ico')

app.mainloop()