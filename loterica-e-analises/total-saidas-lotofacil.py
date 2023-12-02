from sorteios import Lotofacil as LF

#LOTOFACIL

#TOTAL DE SAIDAS, POR NUMERO.

sorteios = LF()

palpite = [2,4,7,10,11,13,14,15,16,19,20,21,23,24,25]

print('Sorteios = ',len(sorteios))
print()

for i in range(len(palpite)):
	
	indice = palpite[i]
	total_saidas = 0
	
	
	for x in sorteios:
		for numero in x:
			if numero == indice:
				total_saidas += 1
				valor = numero
				
	print(' ', palpite[i], ' > ', total_saidas)