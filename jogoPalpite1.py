import random
import os


time = True
erros = 0
sorteado = random.randrange(1,10)


while time != False:
    palpite = int(input('Palpite: '))
    
    if palpite > sorteado:
        print('\nO numero secreto é MENOR\n')
        erros += 1
        
    elif palpite < sorteado:
        print('\nO numero secreto é MAIOR\n')
        erros += 1
    
    else:
        time = False
        
        
os.system('clear')

        
print(f'Parabéns! \n\nTotal de erros = {erros}')