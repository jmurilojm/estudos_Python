opcao=input(' 1 - Real -> Dólar\n 2 - Dólar -> Real\n\n Opação: ')

if opcao == '1':
	dolar=float(input('\nCotação do Dólar: $ '))
	carteira=float(input('Valor a ser convertido (Real): R$ '))
	print(f'\n Em Dólar = $ {carteira/dolar:.2f}')
	
if opcao == '2':
	dolar=float(input('\nCotação do Dólar: $ '))
	carteira=float(input('Valor a ser convertido (Dólar): $ '))
	print(f'\n Em Real = R$ {carteira*dolar:.2f}')