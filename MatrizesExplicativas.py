matriz = []

for qtd_linhas in range(4):
	espaco = []
	for qtd_colunas in range(3):
		item = 0
		espaco.append(item)
	matriz.append(espaco)
	
print(matriz)
	
print()

for cadaEspaco in range(len(matriz)):
	print(matriz[cadaEspaco])
	
print()##########################################

def Matrix(a,b):
	
	matriz = []

	for qtd_linha in range(a):
		espaco = []
		for qtd_colunas in range(b):
			item = 0
			espaco.append(item)
		matriz.append(espaco)
	return print(matriz)
	
Matrix(4,3)

print()##########################################

matriz = []

for qtd_linhas in range(4):
	espaco = []
	for qtd_colunas in range(3):
		item = str(qtd_linhas) + str(qtd_colunas)
		espaco.append(item)
	matriz.append(espaco)
	
print(matriz)

for cadaEspaco in range(len(matriz)):
	print(matriz[cadaEspaco])
	
print()##########################################

compras = []

for totalDeProdutos in range(2):
	espaco = [input('Produto: ')]
	
	for informacoes in range(1):
		quantidade = int(input('Qtd: '))
		espaco.append(quantidade)
		valor = float(input('Und R$: '))
		espaco.append(valor*quantidade)
		
	compras.append(espaco)
	
print(compras)
print()

for cadaEspaco in range(len(compras)):
	print(compras[cadaEspaco])
	
print()##########################################

lista = [[1,2,3],[4,5,6],[7,8,9]]

print('Coluna:    0, 1, 2')
for linha in range(len(lista)):
	print('Linha: ',linha, end = ' ')
	print(lista[linha])
	
print()

for linha in range(len(lista)):
	print(lista[linha][linha], end = ' ')

print()

for linha in range(len(lista)):
	print(lista[linha][linha], end = ' ')
	
