def limpar():
    arquivo = open('txtAgenda.txt','w')
    print('\nFeito!')
    arquivo.close()


def dia():
    import time
    
    dia = time.ctime()
    
    if 'Sun' in dia:
        return 'Domingo'
    elif 'Mon' in dia:
        return 'Segunda-feira'
    elif 'Tue' in dia:
        return 'Terça-feira'
    elif 'Wed' in dia:
        return 'Quarta-feira'
    elif 'Thu' in dia:
        return 'Quinta-feira'
    elif 'Fri' in dia:
        return 'Sexta-feira'
    elif 'Sat' in dia:
        return 'Sábado'


def hora():
    from datetime import datetime
    
    calendario = datetime.now()
    hora = calendario.strftime('%H:%M')
    return hora

        
def data():
    from datetime import datetime
    
    calendario = datetime.now()
    data = calendario.strftime('%d/%m/%y')
    return data


def anotar():
    postit = open('txtAgenda.txt','a')
    
    postit.write(f'\n      {dia()} - {data()}      ')

    stop = True

    while stop != False:
        nota = input('Nota: ')
        postit.write(f'\n{hora()} - {nota}')
    
        continuar = input('Sair? (s/n) ')
        if continuar == 's':
            stop = False
        
    postit.close()


def abrir():
    documento = open('txtAgenda.txt')
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
===============
     AGENDA
===============
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