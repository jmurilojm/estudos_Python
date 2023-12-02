from tkinter import *
from tkinter import messagebox

#caminho = os.path.dirname(__file__)
#nome_arquivo = caminho + '//txtDados.txt'
nome_arquivo = 'data-basic-formulario-simples.txt'
    
formulario = Tk()
formulario.title('Formulário')
formulario.geometry('400x600+800+50')
formulario.configure(background='lightblue')

margem = 20
largura = 360
cor_label = 'lightblue'

Label(text='Nome', bg=cor_label).place(x=margem, y=30)
Label(text='Telefone', bg=cor_label).place(x=margem, y=100)
Label(text='E-mail', bg=cor_label).place(x=margem, y=170)
Label(text='Obs:', bg=cor_label).place(x=margem, y=260)

nome = Entry(bd=3)
nome.place(x=margem, y=50, width=largura)
fone = Entry(bd=3)
fone.place(x=margem, y=120, width=largura)
email = Entry(bd=3)
email.place(x=margem, y=190, width=largura)
obs = Text(bd=3)
obs.place(x=margem, y=280, width=largura, height=200)


def nova():
    '''
    It is function is action to button 'enviar'. It add the elements the a file and show pop-up of the confirmation of shipping.
    '''
    
    n = nome.get()
    f = fone.get()
    e = email.get()
    o = obs.get('1.0', END)
    
    doc = open(nome_arquivo, 'a')
    #Open a file and add elements
    
    doc.write(f'\nNome.......: {n}')
    doc.write(f'\nContato....: {f}')
    doc.write(f'\nE-mail.....: {e}')
    doc.write(f'\nObs........: {o}')
    doc.write('\n')
    
    doc.close()
    
    messagebox.showinfo('', f'Dados salvos com sucesso!')


Button(text='Salvos', bd=3, command=nova, width=10).place(x=margem, y=500)

formulario.mainloop()
