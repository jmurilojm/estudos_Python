# loop_for.py

lista_de_cores = ['Azul', 'Roxo', 'Verde', 'Cinza']
for cor in lista_de_cores:
	print(cor)
	
for cor in lista_de_cores:
	if cor == 'Rosa':
		print('Cor Rosa encontrada')
		break
else:
	print('Cor NAO encontrada')


#range
for i in range(5):
	print('>',i)
	
for i in range(11, -1, -2):
	print(i)
	
for i in range(len(lista_de_cores)):
	print(i,'-', lista_de_cores[i])
	

#enumerate
lista_de_nomes = ['Fulano', 'Beltrano', 'Cicrano']
for i, nome in enumerate(lista_de_nomes):
	print(i, nome)
	

#duas ou mais listas ao mesmo tempo
lista_de_objetos = ['Sapatos', 'Calcas', 'Bones']
lista_de_quantidades = [23,  11, 45]
lista_de_valores = [125.89, 230, 49.90]

for obj, q, val in zip(lista_de_objetos, lista_de_quantidades, lista_de_valores):
	print(obj,'.....',q,'...R$',val)