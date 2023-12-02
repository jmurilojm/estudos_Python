#POST-IT

import os

nota = []
sair = False
centro = 30

while not sair:
	
	anotar = input('Anotar? [s/n] ')
	
	if anotar == 's':
		texto = input('Nota > ')
		nota.append(texto)
		
	print('Anotacões'.center(centro, '='))
	
	for n in nota:
		print(n.center(centro, ' '))
		
	a = input('Sair? [s/n] ')
	if a == 's':
		sair = True
		
	os.system('cls' if os.name == 'nt' else 'clear')