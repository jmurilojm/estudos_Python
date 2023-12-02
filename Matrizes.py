listaMatriz = [[1,2,3],[4,5,6],[7,8,9]]
print(listaMatriz)

listaMatriz[0][1] = 'Murilo'
print(listaMatriz)

listaMatriz.append([10,11,12])
print(listaMatriz)

del listaMatriz[3][1]
print(listaMatriz)

del listaMatriz[3]
print(listaMatriz)

#listaMatriz.clear()
#print(listaMatriz)

listaMatriz[0][1] = 2

print()

for linha in listaMatriz:
	#print(linha)
	for elemento in linha:
		print(elemento,end=' ')
	print()
	
print()
	
soma = 0
for linha in listaMatriz:
	#print(linha)
	for elemento in linha:
		#print(elemento,end=' ')
	#print()
		soma = soma + elemento
		
print(f'Soma: {soma}')
		
print()

lista = [ x**2 for x in range(10)]
print(lista)

lista2 = [ x*2 for x in range(2,10)]
print(lista2)

lista3 = [ n for n in lista2 if n%3==0]
print(lista3)

