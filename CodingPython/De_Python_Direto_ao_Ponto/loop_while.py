# loop_while.py

x = 0

while x < 5:
	print(x)
	x += 1
	

while True:
	resposta = input('A Capital do Brasil? ')
	if resposta == 'brasilia':
		print('Voce acertou!')
		break
	else:
		print('Tente novamente.')
		

while True:
	login = input('Login: ')
	if login != 'admin':
		print('Login invalido')
		continue
	
	senha = input('Senha: ')
	if senha == 'admin1':
		print('Ola, {}!'.format(login))
		print('Acessando...')
		break