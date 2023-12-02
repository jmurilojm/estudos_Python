from tkinter import *

app = Tk()

# Dimensoes da minha janela
largura = 500
altura = 300

# Resolucao da tela pc
# Pega largura da tela
largura_pc = app.winfo_screenwidth()
# Pega altura da tela
altura_pc = app.winfo_screenheight()

# Printando os dados da tela do pc
print(largura_pc, altura_pc)

# Valores para posicao da minha janela no centro
posx = largura_pc/2 - largura/2
posy = altura_pc/2 - altura/2

# Definir a geometry
app.geometry(f'{lagura}x{altura}+{posx}+{posy}')


app.mainloop()