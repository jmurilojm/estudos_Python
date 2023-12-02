# ball_magic.py

import random

sorteio = random.randint(0, 5)

pergunta = input('Faca uma pergunta: ')

if sorteio == 0:
	print('Sim, com certeza.')
elif sorteio == 1:
	print('Parece bom.')
elif sorteio == 2:
	print('Melhor nao te dizer agora.')
elif sorteio == 3:
	print('Nao posso prever agora.')
elif sorteio == 4:
	print('Nao conte com isso.')
elif sorteio == 5:
	print('Minhas fontes dizem nao.')