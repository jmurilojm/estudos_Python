#ARGS

def imc(*args):
	''' Faz a soma de varios argumentos'''
	soma = 0
	for i in args:
		soma += i
	print(soma)
	
imc()

print(help(imc))