anotacoes = []
opcao = input('Deseja fazer uma anotacao? (s/n) ')

while opcao != 'n':
    
    if opcao == 's':
        anotacao = input('Nota: ')
        anotacoes.append(anotacao)
        
        continuar = input('Sair? (s/n) ')
        if continuar == 's':
            break


print('\nFinalizado!\n')

def post_it(lista):
    
    titulo = 'NOTAS'
    caractere = '='
    detalhe = (len(titulo)+16)*caractere
    
    print(detalhe)
    print(titulo.center(len(detalhe)))
    print(detalhe)
    
    for n in lista:
        print(n)
        


post_it(anotacoes)