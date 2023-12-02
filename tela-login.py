#TELA_LOGIN

print('User: admin | Senha: 999 \n')

while True:
	n = str(input('User: '))
	
	if n != 'admin':
		print('Usuário não encontrado.')
		continue
		
	s = int(input('Senha: '))
	if s != 999:
		print('Verifique sua senha.')
		continue
		
	else:
		print('\nEntrando...')
		break