'''
GERENCIADORES DE LAYOUT

.title
.geometry()
# LxA+E+T

Posicao onde vai aparecer a janela:

L - width - Largura
A - heith - Altura
E - left - espaco esquerdo - eixo x
T - too - espaco acima - eixo y

'''

from tkinter import *

app = Tk()


app.title = 'Titulo'
app.geometry('10x10+80+80')
app.mainloop()