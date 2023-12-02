from sorteios import MegaSena as MS

#CONFERIR PALPITES + VARIOS SORTEIOS

#=============SORTEIOS===============

sorteios = MS()

#=============PALPITES===============

palpite= [[10, 20, 25, 30, 33, 34, 48], [23,27,30,19,24,25], [3,51,55,18,45,9]]

#=============ANALISE================

print('Sorteio 1')
for i in range(len(sorteios)):
	for x in palpite:
		n = []
		for y in x:
			if y in sorteios[i]:
				n.append(y)
		
		print(f' Palpite {x} > {n} - Total: {len(n)}')
	print(f'\nSorteio {i+2}')