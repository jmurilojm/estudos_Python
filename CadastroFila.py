fila=list()
atendidos=list()

menu=int(input('1 - Cadastrar\n2 - Fila\n0 - Sair\n\n>>> '))

while menu != 0:
	
	#cadastro
	if menu == 1:
		fila.append(str(input('\nNome: ').title()))
		print('\nO Cadastro foi realizado!\n')
		menu=int(input('1 - Cadastrar\n2 - Fila\n0 - Sair\n\n>>> '))
		
	#mostrar fila
	elif menu == 2:
		if len(fila) == 0:
			print('\nFila esta vazia!\n')
			menu=int(input('1 - Cadastrar\n2 - Fila\n0 - Sair\n\n>>> '))
		else:
			'''for n in range(len(fila)):
				print(fila[n])'''
			print('\n',fila,'\n')
			menu=int(input('1 - Cadastrar\n2 - Fila\n0 - Sair\n\n>>> '))
		
print('\nFinalizado!')