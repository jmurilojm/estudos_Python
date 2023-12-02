from tkinter import *
from tkinter import messagebox
import os

#caminho = os.path.dirname(__file__)
#nome_arquivo = caminho + '//txtDados.txt'
nome_arquivo = 'data-basic-formulario-simples.txt'
    
envio = Tk()

Label(text='Nome*').place(x=20,y=20)
Label(text='Telefone*').place(x=20,y=200)
Label(text='E-mail*').place(x=20,y=380)
Label(text='Obs:').place(x=20,y=560)
Label(text='"*" Obrigatórios.').place(x=20,y=2050)

nome = Entry(bd=3)
nome.place(x=20,y=90,width=1040)
fone = Entry(bd=3)
fone.place(x=20,y=270,width=1040)
email = Entry(bd=3)
email.place(x=20,y=450,width=1040)
obs = Text(bd=3)
obs.place(x=20,y=630,width=1040)

def nova():
    '''
    It is function is action to button 'enviar'. It add the elements the a file and show pop-up of the confirmation of shipping.
    '''
    
    n = nome.get()
    f = fone.get()
    e = email.get()
    o = obs.get('1.0',END)
    
    doc = open(nome_arquivo,'a')
    #Open a file and add elements
    
    doc.write(f'\nNome.......: {n}')
    doc.write(f'\nContato....: {f}')
    doc.write(f'\nE-mail.....: {e}')
    doc.write(f'\nObs........: {o}')
    doc.write('\n')
    
    doc.close()
    
    messagebox.showinfo('',f'Dados salvos com sucesso!')
    
Button(text='Salvar',bd=3,command=nova).place(x=20,y=1850)

envio.mainloop()