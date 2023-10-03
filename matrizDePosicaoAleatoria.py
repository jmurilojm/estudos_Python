import random

valorAleatorio = random.randint(1,20)
valorAleatorio2 = random.randint(1,20)

for linha in range(1,21):
    for coluna in range(1,21):
        if linha == valorAleatorio and coluna == valorAleatorio2:
            print('  ',end='')
            continue
        print([] ,end='')
        
    print()
    

print('\nPosicao: ',valorAleatorio,'x',valorAleatorio2)