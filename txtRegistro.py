def limpar():
    arquivo = open('txtRegistro.txt','w')
    print('\n Processo de limpeza realizado com sucesso!')
    arquivo.close()


def dia():
    import time
    
    dia = time.ctime()
    
    if 'Sun' in dia:
        return 'DOM'
    elif 'Mon' in dia:
        return 'SEG'
    elif 'Tue' in dia:
        return 'TER'
    elif 'Wed' in dia:
        return 'QUA'
    elif 'Thu' in dia:
        return 'QUI'
    elif 'Fri' in dia:
        return 'SEX'
    elif 'Sat' in dia:
        return 'SÁB'


def hora():
    from datetime import datetime
    
    calendario = datetime.now()
    hora = calendario.strftime('%H:%M')
    return hora
    
    
def turno():
    from datetime import datetime
    
    calendario = datetime.now()
    hora = calendario.strftime('%H')
    if int(hora) < 12:
        return 'Matutino'
    else:
        return 'Vespertino'

        
def data():
    from datetime import datetime
    
    calendario = datetime.now()
    data = calendario.strftime('%d/%m/%y')
    return data


def anotar():
    postit = open('txtRegistro.txt','a')
    
    #postit.write(f'\n      {dia()} - {data()}')

    stop = True

    while stop != False:
        nota = input('\n Nome.....: ').title()
        if nota == '0':
            stop = False
        else:
            sala = int(input(' Sala.....: '))
            h = int(input(' Horas....: '))
            t = 'Matutino' if h < 12 else 'Vespertino'
            m = int(input(' Minutos..: '))
            obs = input(' Obs......: ')
            #postit.write(f'\n{hora()} - {nota} - {sala} - {turno()}')
            postit.write(f'\n{data()} {dia()} _ {h}:{m} _ {nota} _ {sala} _ {t} _ Obs: {obs}')
        
    postit.close()


def abrir():
    documento = open('txtRegistro.txt')
    print(documento.read())
    documento.close()


def acao(numero):
    if numero == 1:
        anotar()
    elif numero == 2:
        abrir()
    elif numero == 3:
        limpar()


def menu():
    opcao = True
    
    while opcao != False:
        opcao = int(input('''
==================
     REGISTRO
==================
    1 - Anotar
    2 - Exibir
    3 - limpar
    0 - Sair

>> '''))
        if opcao == 1:
            acao(1)
        elif opcao == 2:
            acao(2)
        elif opcao == 3:
            acao(3)
        elif opcao == 0:
            opcao = False



    
menu()