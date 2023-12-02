print(22*'=','SISTEMA DE CADASTROS',22*'=','\n')

opcao=''
cadastros=list()

while opcao != 0:
	print('== MENU DE OPCOES ==')
	print(' 1 - Cadastrar')
	print(' 2 - Mostrar Lista')
	print(' 3 - Remover')
	print(' 4 - Consultar')
	print(' 0 - sair')
	print(20*'=')
	
	opcao = int(input('\n      Opcao: '))
	print()
	
	#Caso 1: Cadastro
	if opcao == 1:
		cadastros.append(input('Digite nome: '))
		print('\n       Feito!\n')
	
	#Caso 2: Lista e Total
	elif opcao == 2:
		print(cadastros,'\n')
		print('Total cadastrados: ',len(cadastros),'\n')
	
	#Caso 3: Remover
	elif opcao == 3:
		print('Cadastrados: ',cadastros)
		nome=input('\nQuem voce deseja remover? ')
		if nome in cadastros:
			cadastros.remove(nome)
			print('\n      Removido!')
			print()
		else:
			print('\n    Sem cadastro!\n')
	
	#Caso 4: Consulta
	elif opcao == 4:
		nome=input('Digite nome: ')

		if nome in cadastros:
			posicao=cadastros.index(nome)
			print()
			print('    Encontrado!')
			print('\nPosicao: ',(posicao+1))
			print()
			
			sn=input('\nDeseja remover [s/n]: ')
			
			if sn == 's':
				cadastros.remove(nome)
				print('\n      Removido!\n')
				print('Agora temos',len(cadastros),'cadastros.\n')
			elif sn == 'n':
				print()
				
		else:
			print('\n    Sem cadastro!\n')
	
	
print('     Finalizado!')
print('\nDeveloped by ©JMurilo - 2021.\n\n\n\n\n')