#CONDICOES If, Elif e Else

#Par ou Impar
x=10

print(f'O numero {x} é ?')
print()

if x % 2 == 0:
	print(' Resposta: É um numero PAR')
else:
	print(' Resposta: É um numero IMPAR')
	
print(34*'_ ')
	
#Maior ou Menor
a=110
b=25

print(f'a={a} e b={b}')

if a>b:
	print(' Resposta: A é maior que B')
elif a==b:
	print(' Resposta: A é igual a B')
else:
	print(' Resposta: A é menor que B')
	
print(34*'_ ')

#Usando and \ or

pagou=True
maior=True

print(f'Status: Pagou={pagou} e Maior={maior}')

if pagou and maior:
	print(' Resposta: Liberado!')
else:
	print(' Resposta: Impedido!')

#Fim