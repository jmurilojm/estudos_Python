#LOOP FOR

for x in range(10):
	print(x, end=' ')

print()
print(34*'_ ')
	
for x in range(1,11):
	print(x, end=' ')
	
print()
print(34*'_ ')

for x in range(1,46,2):
	print(x, end=' ')

print()
print(34*'_ ')

lista=['Murilo','Jessica','Douglas','Danilo']

for elemento in lista:
	print(elemento)
	
print(34*'_ ')
	
#Utilizando LEN

nome='Murilo'

print(len(nome))
print(len(lista))
print(34*'_ ')

for elementoNestaPosicao in range(len(lista)):
	print( lista[ elementoNestaPosicao ] )

#Fim