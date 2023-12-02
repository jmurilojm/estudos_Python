import PySimpleGUI as sg

class TelaPy:
    def __init__(self):
        
        #Layout
        modelo = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=20)],
            [sg.Text('Senha',size=(5,0)),sg.Input(size=20)],
            [sg.Button('Enviar dados')]
        ]
        
        #Janela
        janela = sg.Window('Dados do Usuario').layout(modelo)
        
        #Extrair dados da tela
        self.button, self.values = janela.Read()
        
    def Iniciar(self):
        print(self.values)



tela = TelaPy()
tela.Iniciar()