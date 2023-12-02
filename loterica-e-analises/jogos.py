#==============JOGOS================
'''
Dias:
	Seg: Lotofacil, Lotomania
	Ter: Lotofacil, Dia de Sorte
	Qua: Lotofacil, MegaSena, Lotomania
	Qui: Lotofacil, Dia de Sorte
	Sex: Lotofacil, Lotomania
	Sab: Lotofacil, MegaSena, Dia de Sorte

Valores:
	MegaSena = 5,50
	Lotofacil = 2,50
	Lotomania = 2,50
	Dia de Sorte = 3,00
	
Acertos:
	MegaSena:
		4, 5, ou 6 em 6 de 60
	Lotofacil: 
		11, 12, 13, 14 ou 15 em 15 de 25
	Lotomania: 
		15, 16, 17, 18, 19 ou 20 em 50 de 100
	Dia de Sorte: 
		4, 5, 6 ou 7 em 7 de 31
'''

#============MEGA-SENA==============
def AnaliseMegaSena(palpite):
	'''
	É necessário que repasse uma lista com os números para serem analisados.
	'''
	from sorteios import MegaSena as MS
	
	sorteios = MS()
	print(f'MEGASENA - {len(sorteios)} jogos.\n')
	
	for i in range(len(sorteios)):
	
		numeros = [] 
	
		for x in range(len(palpite)):
			if palpite[x] in sorteios[i]:
				numeros.append(palpite[x])
		print(f' > {len(numeros)} - {numeros}')
		
		
def AnaliseIntuitivaMegaSena():
	from sorteios import MegaSena as MS
	
	palpite = []

	for i in range(6):
		palpite.append(int(input(f'{i+1}⁰ > ')))
	
	sorteios = MS()
	print(f'MEGASENA - {len(sorteios)} jogos.\n')
	
	print()
	for i in range(len(sorteios)):
	
		numeros = [] 
	
		for x in range(len(palpite)):
			if palpite[x] in sorteios[i]:
				numeros.append(palpite[x])
		print(f' > {len(numeros)} - {numeros}')

		
#=============LOTOFACIL==============
def AnaliseLotofacil(palpite):
	'''
	É necessário que repasse uma lista com os números para serem analisados.
	'''
	from sorteios import Lotofacil as LF
	
	sorteios = LF()
	print(f'LOTOFACIL - {len(sorteios)} jogos.\n')
	
	for i in range(len(sorteios)):
	
		numeros = []
	
		for x in range(len(palpite)):
			if palpite[x] in sorteios[i]:
				numeros.append(palpite[x])
	
		print(f' > {len(numeros)} - {numeros}')
	
#============LOTOMANIA==============
def AnaliseLotomania(palpite):
	'''
	É necessário que repasse uma lista com os números para serem analisados.
	'''
	from sorteios import Lotomania as LM
	
	sorteios = LM()
	print(f'LOTOMANIA - {len(sorteios)} jogos.\n')
	
	for i in range(len(sorteios)):
	
		numeros = [] 
	
		for x in range(len(palpite)):
			if palpite[x] in sorteios[i]:
				numeros.append(palpite[x])
				
		print(f' > {len(numeros)} - {numeros}')

#===========DIA_DE_SORTE=============
def AnaliseDiaDeSorte(palpite):
	'''
	É necessário que repasse uma lista com os números para serem analisados.
	'''
	from sorteios import DiaDeSorte as DS
	
	sorteios = DS()
	print(f'DIA DE SORTE - {len(sorteios)} jogos.\n')
	
	for i in range(len(sorteios)):
	
		numeros = [] 
	
		for x in range(len(palpite)):
			if palpite[x] in sorteios[i]:
				numeros.append(palpite[x])
				
		print(f' > {len(numeros)} - {numeros}')
		
		
#==========MAIS_MILIONARIA============
def AnaliseMaisMilionaria(palpite):
	'''
	É necessário que repasse uma lista com os números para serem analisados.
	'''
	from sorteios import MaisMilionaria as MM
	
	sorteios = MM()
	print(f'Mais Milionária - {len(sorteios)} jogos.\n')
	
	for i in range(len(sorteios)):
	
		numeros = [] 
	
		for x in range(len(palpite)):
			if palpite[x] in sorteios[i]:
				numeros.append(palpite[x])
				
		print(f' > {len(numeros)} - {numeros}')
		
def AnaliseMaisMilionariaTrevo(palpite):
	'''
	É necessário que repasse uma lista com os números para serem analisados.
	'''
	from sorteios import MaisMilionariaTrevo as MMT
	
	sorteios = MMT()
	print(f'\nTrevo\n')
	
	for i in range(len(sorteios)):
	
		numeros = [] 
	
		for x in range(len(palpite)):
			if palpite[x] in sorteios[i]:
				numeros.append(palpite[x])
				
		print(f' > {len(numeros)} - {numeros}')