#CODIGO BASE - CONFEFENCIA DE JOGOS

#conjunto de listas disponiveis:
conj = [[2,4,6,7,11,12,13,14,15,17,18,19,22,23,25], [1,3,5,8,10,11,12,13,14,16,18,19,20,21,25],[2,5,7,8,9,10,11,12,13,16,18,19,20,21,23]]

#lista com numeroa para serem conferidos:
unica = [2,4,5,6,8,9,10,12,13,14,19,20,21,22,25]


for i in range(len(conj)):
	'''
	Este for percorrera o total de listas do conjunto.
	'''
	numeros = [] 
	'''esta lista armazena os numeros depois do print é zerada para poder armazenar a proxima conferencia.
	'''
	
	for x in range(len(unica)):
		if unica[x] in conj[i]:
			numeros.append(unica[x])
	
	print(f' Verificação da {i+1}ª lista do conjunto:')
	print(f' {numeros} > {len(numeros)} números encontrados.\n')#print dos numeros apos cada verificacao.