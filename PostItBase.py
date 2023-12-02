anotacoes = []

stop = True

while stop != False:
    nota = input('Nota: ')
    anotacoes.append(nota)
    
    continuar = input('Sair? (s/n) ')
    if continuar == 's':
        stop = False
        
print(anotacoes)