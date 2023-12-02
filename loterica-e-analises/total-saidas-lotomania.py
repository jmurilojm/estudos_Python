from sorteios import Lotomania as LM

#LOTOMANIA

#TOTAL DE SAIDAS, POR NUMERO.

#============SORTEIOS===============

sorteios = LM()

#=============PALPITE=================

a = [1,3,5,7,9,11,13,15,17,19,20,22,23,26,28,32,35,37,38,39,42,43,45,46,48,49,51,52,54,56,58,60,66,67,69,70,71,72,73,78,82,84,86,89,91,93,95,97,98,00]#13

b=[2,7,10,13,14,19,20,22,23,26,28,29,32,33,35,36,38,40,41,43,48,49,50,53,56,57,60,62,64,66,67,69,71,72,76,77,80,81,82,84,85,86,88,90,92,94,95,97,99,00]#13 14 15

jogada = [2,7,10,13,14,19,20,22,23,26,28,29,32,33,35,36,38,40,41,43,48,49,50,53,56,57,60,62,64,66,67,69,71,72,76,77,80,81,82,84,85,86,88,90,92,94,95,97,99,00]


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