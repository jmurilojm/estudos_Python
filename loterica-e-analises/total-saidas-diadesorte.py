from sorteios import DiaDeSorte as DS

#DIA DE SORTE

#TOTAL DE SAIDAS, POR NUMERO.

#============SORTEIOS===============

sorteios = DS()

#=============PALPITE=================

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

letra = a
print('\n > Palpite: ',letra,len(letra),'\n')
palpite = letra

#============VERIFICACAO=============

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