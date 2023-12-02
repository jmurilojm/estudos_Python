opcao = ''

while opcao != 0:

	opcao = int(input('Numero: '))

	x = 'Par' if opcao%2 == 0 else 'Impar'

	print(x)
	
print()
print('Fim...')