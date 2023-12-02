lista = []

lista.append(45)
print(lista)

lista.append(73)
print(lista)

lista2 = lista

print(id(lista))
print(id(lista2))
#del lista[1]
print(lista)
print(lista2)

lista3 = lista[:]

print(id(lista))
print(id(lista3))

del lista3[1]
print(lista)
print(lista3)

lista3.append('Eu')
print('Lista',lista)
print('Lista 3',lista3)

lista = lista3[:]

print('Lista',lista)

if 'E' in lista:
	print('Tem')
	lista.remove('Eu')
	
else:
	print('Nao')
	

print(lista)