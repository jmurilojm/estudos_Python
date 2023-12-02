def soma(*numeros): #desempacotamento
	soma = 0
	for numero in numeros:
		soma += numero
	print(soma)
	pass
	
	
soma(2,3,4,5)