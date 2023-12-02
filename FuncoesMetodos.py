def somar(a,b):
	return a+b
	
def subtrair(a,b):
	return a-b
	
def multiplicar(a,b):
	return a*b
	
def dividir(a,b):
	return a/b
	
def potencia(a,b):
	print(f'Potenciacao: ',a**b)
	
def resto(a,b):
	print('Resto da divisao: ',a%b)
	
def parteInteira(a,b):
	print('Parte inteira da divisao: ',a//b)
	
print('Operacoes com os numeros: 9 e 6 :\n')
print(f'Soma: ',somar(9,6))
print(f'Subtracao: ',subtrair(9,6))
print(f'Multiplicacao: ',multiplicar(9,6))
print(f'Divisao: ',dividir(9,6),'\n')

potencia(9,6)
resto(9,6)
parteInteira(9,6)