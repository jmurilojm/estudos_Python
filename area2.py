import PySimpleGUI as sg

#O que vai ter no Layout?
lay = [

    [sg.Text('Base:', size=6), sg.InputText(key='base', size = (10,1))],
    [sg.Text('Altura:',size=6), sg.InputText(key='altura', size=(10,1))],
    [sg.Button('Calcular')],
    [sg.Text('', key='out')]
    
]

# Criando a Janela!
jan = sg.Window('Cálculo de Área²',lay)

while True:
    evento, valor = jan.read()
    
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Calcular':
        dados = int(valor['base']) * int(valor['altura'])
        jan['out'].update('Área total = ' + str(dados) + 'm²')

jan.close()