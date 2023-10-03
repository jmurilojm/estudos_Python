def linha(): #linhas
	print('=' * 20)
	print()

def campoTexto(texto): #com parametro
	tam=len(texto) + 4
	print('=' * tam)
	print(' ',texto)
	print('=' * tam)
	print()

def soma(*a): #desempacotamento
	somado=0
	for num in a:
		somado+=num
	print(somado)
	print()


linha()
campoTexto('Fulano de Tal')
soma(4,8)


def velocidade(espaco,tempo):
	v = espaco/tempo
	print(v)
	pass

def comprimentar():
	print('\nOi!')
	pass
	
def dados(nome,idade=None):
	print(nome)
	print(idade)
	pass
	
def soma(a,b):
	return a+b,a-b,a*b
	pass
	
def calc(a,b):
	return {'Soma':a+b,'Multiplicacao':a*b}
	pass
	
def argumentos(arg,*args):
	print(arg)
	print(args)
	pass
	
#velocidade
velocidade(180,1.5)

#comprimentar
comprimentar()

#dados
dados('Murilo')

#soma
print(soma(15,76))

#calc
print(calc(16,75))

valor=calc(25,5)
for key in valor:
	print(key,'= ',valor[key])
	
#argumenentos
argumentos(5,1,2,3,4)