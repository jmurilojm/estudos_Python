from tkinter import *

class App:
    def __init__(self, master=None):
        self.fontePadrao = ('Arial','10')
        
        # CONTAINERS
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer['pady'] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer['pady'] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer['pady'] = 20
        self.quartoContainer.pack()

        # 1º - TÍTULO 
        self.titulo = Label(self.primeiroContainer)
        self.titulo['text'] = 'Dados do usuário'
        self.titulo['font'] = ('Arial','10','bold')
        self.titulo.pack()

        # 2º - NOME
        self.nomeLabel = Label(self.segundoContainer)
        self.nomeLabel['text'] = 'Nome'
        self.nomeLabel['font'] = self.fontePadrao
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.segundoContainer)
        self.nome['width'] = 30
        self.nome['font'] = self.fontePadrao
        self.nome.pack(side=RIGHT)

        # 3º - SENHA
        self.senhaLabel = Label(self.terceiroContainer)
        self.senhaLabel['text'] = 'Senha'
        self.senhaLabel['font'] = self.fontePadrao
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.terceiroContainer)
        self.senha['width'] = 30
        self.senha['font'] = self.fontePadrao
        self.senha['show'] = '*'
        self.senha.pack(side=RIGHT)

        # 4º - BOTÃO DE AUTENTICAÇÃO
        self.autenticar = Button(self.quartoContainer)
        self.autenticar['text'] = 'Autenticar'
        self.autenticar['font'] = ('Arial','8','bold')
        self.autenticar['width'] = 12
        self.autenticar['command'] = self.verificarSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer)
        self.mensagem['text'] = ''
        self.mensagem['font'] = self.fontePadrao
        self.mensagem.pack()

    # MÉTODO VERIFICAR SENHA
    def verificarSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        if usuario == 'Admin' and senha == '1':
            self.mensagem['text'] = "Autenticado!"
        else:
            self.mensagem['text'] = 'Erro na autenticação!'

        pass


janela = Tk()
App(janela)
janela.mainloop()