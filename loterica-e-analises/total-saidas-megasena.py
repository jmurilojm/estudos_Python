from sorteios import MegaSena as MS

#MEGA SENA

#TOTAL DE SAIDAS, POR NUMERO.

#sorteios = MS()
sorteios = [['Mar', 6, 7, 25, 28, 31, 52],
	[8, 18, 26, 27, 47, 50],
	[9, 18, 33, 38, 41, 51],
	[3, 7, 15, 22, 24, 50],
	[6, 26, 32, 35, 37, 49],
	[12, 17, 43, 44, 48, 60]]

print('Sorteios: ',len(sorteios))
print()

numeros = {}

for i in range(1,61):
	
	total_saidas = 0
	
	for x in sorteios:
		for numero in x:
			if numero == i:
				total_saidas += 1
				valor = numero
	print(' ', i , ' > ', total_saidas)
#################################
	'''numeros[i] = total_saidas

print()
print(numeros)

num = list()
for i in numeros.values():
	num.append(i)

num.append(999)
listaOrdenada = sorted(num)

listaInvertida = list(reversed(listaOrdenada))

print()
print(num)
print()
print(listaOrdenada)
print()
print(listaInvertida)
print()'''

'''for i in range(len(num)):
	#Tentando fazer a busca da chave desse valor.
	if listaInvertida[i] in numeros.values():
		print('sim')
		
	else:
		print('nao')'''