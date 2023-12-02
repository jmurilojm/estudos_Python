import random
import os


erros = 0
sorteado = random.randrange(1,10)


palpite = int(input('Palpite: '))


while palpite != sorteado:
    os.system('clear')
    if palpite > sorteado:
        print('O numero secreto é MENOR\n')
        
    elif palpite < sorteado:
        print('O numero secreto é MAIOR\n')
        
    erros += 1
    
    palpite = int(input('Palpite: '))

        
print(f'\nParabéns! \n\nTotal de erros = {erros}')