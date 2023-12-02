import tkinter

# Análise dos dados e retorno da análise
def clique():
    nome = usuario.get()
    codigo = senha.get()
    
    if codigo == '1' and nome == 'Admin':
        label4['text'] = 'Acessando...'
    else:
        label4['text'] = 'Verifique sua Senha ou Usuário!'


janela = tkinter.Tk()

janela.title('Login')
janela.geometry('160x110')


# FRAME 0 - Título
frame0 = tkinter.Frame(janela,)
frame0.pack(fill='both', padx=10, pady=100)

label0 = tkinter.Label(frame0,text='Acesso:')
label0.pack()

# FRAME 1 - Id
frame1 = tkinter.Frame(janela,)
frame1.pack(fill='both', padx=10, pady=5)

label1 = tkinter.Label(frame1,text='Usuário')
label1.pack(side='left')

usuario = tkinter.Entry(frame1, width=20)
usuario.pack(side='right')

# FRAME 2 - Senha
frame2 = tkinter.Frame(janela,)
frame2.pack(fill='both', padx=10, pady=5)

label2 = tkinter.Label(frame2, text='Senha')
label2.pack(side='left')

senha = tkinter.Entry(frame2, width=20, show='*')
senha.pack(side='right')

# FRAME 3 - Botao
frame3 = tkinter.Frame(janela,)
frame3.pack(fill='both', padx=10, pady=100)

butao = tkinter.Button(frame3, text='Logar', command = clique)
butao.pack()

# FRAME 4 - Mensagem de confirmacao
frame4 = tkinter.Frame(janela,)
frame4.pack(fill='both', padx=10, pady=100)

label4 = tkinter.Label(frame4, text='')
label4.pack()



# Main
janela.mainloop()