def limpar():
    arquivo = open('agenda.txt','w')
    arquivo.write('=============== NOTAS ===============')
    print('\nFeito!')
    arquivo.close()


def anotar():
    import time

    postit = open('agenda.txt','a')

    stop = True

    while stop != False:
        data = time.ctime()
        
        nota = input('Nota: ')
        if nota != '0':
            postit.write(f'\n{data} - {nota}')
        else:
            stop = False
        
    postit.close()


def abrir():
    documento = open('agenda.txt')
    print(documento.read())
    documento.close()


def acao(numero):
    if numero == 1:
        anotar()
    elif numero == 2:
        abrir()
    elif numero == 3:
        limpar()


def anotar():
    opcao = True
    
    while opcao != False:
        opcao = int(input('''
===============
     MENU
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



    
anotar()