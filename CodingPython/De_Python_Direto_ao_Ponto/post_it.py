# post_it.py

import os

notas = []
sair = False

while not sair:
	'''anotar = input('Anotar? (s/n) ')
	
	#escrever nota
	if anotar == 's':
		texto = input('Nota: ')
		notas.append(texto)'''
		
	texto = input('Nota: ')
	notas.append(texto)
	
	#layout
	print('\n' + ' Anotacoes '.center(30, '='))
	for nota in notas:
		print(nota.center(30))
	print(30 * '=')
		
	#sair
	indagar = input('Sair? (s/n) ')
	if indagar == 's':
		sair = True
	
	#limpar tela
	os.system('cls' if os.name == 'nt' else 'clear')
	
print(notas)