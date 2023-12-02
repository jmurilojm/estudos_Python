from PySimpleGUI import PySimpleGUI as ps

#Lyout
ps.theme('Reddit')

modelo = [
    [ps.Text('Nome'), ps.Input(key = 'u',size=20)],
    [ps.Text('Chave'), ps.Input(key = 's',password_char='*',size=20)],
    [ps.Checkbox('Salvar?')],
    [ps.Button('Entrar')]
]

#Janela
tela = ps.Window('Tela de Login', modelo)

#Ler eventos
while True:
    eventos, valores = tela.read()
    
    if eventos == ps.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['u'] == 'Murilo' and valores['s'] == 123:
            print('Acessado!')