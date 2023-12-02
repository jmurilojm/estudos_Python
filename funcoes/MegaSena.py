def palpites(quantidadeDesejada):
	from random import randint
	print()
	
	contador = 0
	
	while contador < quantidadeDesejada:
		palpite = []

		while len(palpite) < 6:
			numeroSorteado = randint(1, 60)
	
			if numeroSorteado not in palpite:
				palpite.append(numeroSorteado)
		
		print(f'> {contador + 1}  > {sorted(palpite)}')
		
		contador += 1
		pass
		

palpites(6)