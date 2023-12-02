import PySimpleGUI as sg


# Escolhendo um tema.
sg.theme('Lightblue')


# O que vai ter na Janela:
layout = [

    [sg.Text('Digite algo abaixo.')],
    [sg.Text('Texto:'), sg.InputText(size = 20)],
    [sg.Button('Ok'), sg.Button('Cancelar')]
    
    ]

# Criando a janela:
janela = sg.Window('Programa Textos', layout)

# Iniciando o programa:
while True:
    evento, valor = janela.read()
    
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        # Ao fechar ou clicar em cancelar.
        break
    print('Você digitou: ', valor[0])


janela.close()