import os

def layout_nota(lista_de_notas):
    '''
    Imprime as notas dentro de um layout pre-definido.
    
    Exemplo:
        ============
        > a
        > b
        > c
        ============
        
    '''
    print(15*'=')
    for nota in lista_de_notas:
        print('>',nota)
    print(15*'=')
    
help(layout_nota)

notas = []
sair = False


while not sair:
    anotacao = input('Nota: ')
    os.system('clear')
    
    if anotacao == 'sair':
        layout_nota(notas)
        break
    else:
        notas.append(anotacao)
    
    layout_nota(notas)