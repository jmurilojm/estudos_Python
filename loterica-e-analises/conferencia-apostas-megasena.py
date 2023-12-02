#CONFERENCIA DAS APOSTAS

#Apostadores

nomes = ['ednaldo','mene','ale','rosy','socorro','jo','didi','rosane','ju','jm']

apostas = [[2 , 6 , 17 , 40 , 44 , 53], 
					[27 , 3 , 40 , 18 , 11 , 19], 
					[2 , 10 , 33 , 43 , 25 , 17], 
					[7 , 11 , 15 , 18 , 24 , 29], 
					[1 , 3 , 5 , 39 , 49 , 60], 
					[13 , 15 , 26 , 28 , 48 , 45], 
					[17 ,  20 , 22 , 35 , 41 , 42], 
					[3 , 12 , 17 , 20 , 35 , 40], 
					[2 , 13 , 25 , 38 , 43 , 57], 
					[11 , 14 , 25 , 32 , 38 , 45]]

#=============SORTEIO=================
sorteio = [6, 7, 25, 28, 31, 52]#1.03
print()

#============VERIFICACAO==============
for i in range(len(apostas)):
	
	numeros = [] 
	
	for x in range(len(sorteio)):
		if sorteio[x] in apostas[i]:
			numeros.append(sorteio[x])
	print(f' > {len(numeros)} - {nomes[i]} - {numeros}')