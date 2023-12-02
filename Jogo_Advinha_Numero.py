#JOGO ADVINHA NUMERO

import random

print('Seja bem vindo!')

sorteado=random.randint(1,101)
print(sorteado)

chances=1

nome=input('Nome: ')
print('Voce tera 07 chances.')
print(f'Chance numero {chances}')
chances += 1
palpite=int(input('Palpite: '))

tentativas=1

while tentativas<7:
	if palpite>sorteado:
		print('É menor!')
		print(f'Chance numero {chances}')
		chances += 1
		palpite=int(input('Palpite: '))
		tentativas += 1
	elif palpite<sorteado:
		print('É maior!')
		print(f'Chance numero {chances}')
		chances += 1
		palpite=int(input('Palpite: '))
		tentativas += 1
	elif palpite == sorteado:
		print('Parabens!')
		print(f'Voce acertou na tentativa {chances-1}')
		break
		
	if chances == 7:
		print('Esta é sua ULTIMA chance!')

#Fim!