# compras.py

import os

produtos = []
valores = []
quantidades = []
sair = False

while not sair:
	print(' Produtos '.center(40,'='))
	for i in range(len(produtos)):
		calculo = quantidades[i] * valores[i]
		print(quantidades[i],'un -',produtos[i],'...R$',valores[i])
	
	produtos.append(input('Produto: '))
	valores.append(float(input('Valor: ')))
	quantidades.append(int(input('Quantidade: ')))
	
	indagar = input('Sair? (s/n) ')
	if indagar == 's':
		sair = True
		
	os.system('cls' if os.name == 'nt' else 'clear')
		

valor_total = 0
print(' Produtos '.center(40,'='))
for i in range(len(produtos)):
	calculo = quantidades[i] * valores[i]
	valor_total += calculo
	
	print(quantidades[i],'un -',produtos[i],'.....R$',valores[i])


print('\n\nTotal:..........................',valor_total)