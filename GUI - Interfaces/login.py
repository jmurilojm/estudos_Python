import tkinter

janela = tkinter.Tk()


janela.title('Login')
janela.geometry('160x110')

# FRAME 0 - Título
frame0 = tkinter.Frame(janela,)
frame0.pack(fill='both', padx=10, pady=5)

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


# Main
janela.mainloop()