# listas.py

lista_de_frutas = ['Uva', 'Laranja', 'Mamao', 'Acerola']

print('Total de itens = {}'.format(len(lista_de_frutas)))

print(lista_de_frutas[1])
print(lista_de_frutas)

lista_de_frutas[2] = 'Goiaba'
print(lista_de_frutas)


#adicionar elementos
#concatenando
lista_de_numeros = [23, 11, 45]
nova_lista = lista_de_frutas + lista_de_numeros

print(nova_lista)

#lista.append()
nova_lista.append(100)
print(nova_lista)

#lista.insert(indice, item)
nova_lista.insert(1, 'ABACATE')
print(nova_lista)


#remover elementos
#lista.pop()
nova_lista.pop()
print(nova_lista)

nova_lista.pop(-2)
print(nova_lista)

#lista.remove(item)
nova_lista.remove('Goiaba')
print(nova_lista)


#outros metodos
#lista.sort()
numeros = [6, 2, 8, 1, 0, 3, 9, 5, 4, 7]

numeros.sort()
print(numeros)

#lista.reverse()
numeros.reverse()
print(numeros)


#mutaveis e imutaveis
#imutavel
x = 'amor'
print(x, id(x))
x = x.upper()
print(x, id(x))

#mutavel
y = [4,7,3,1,8]
print(y, id(y))
y.sort()
print(y, id(y))


#listas aninhadas
ninho = [102, 203, ['ab', 'bc', 'cd'], 304]
print(ninho)
print(ninho[0])
print(ninho[2])
print(ninho[2][1])


#copiando listas
#nao e uma copia
li = [7]
print(id(li))
lii = li
print(id(lii))
lii.append(5)
print(id(lii))
print(li,'-',lii)
li.pop()
print(li,'-',lii)
print(li is lii)

#copia com lista[:] ( chamdo slice)
a = [93, 54]
b = a[:]
print('Com slice',a, b)
print(id(a))
print(id(b))
a.pop()
print(a, b)
print(a is b)

#copia com lista.copy()
c = [32, 76, 98]
d = c.copy()
print('Com copy()',c, d)
print(id(c))
print(id(d))
c.pop()
print(c, d)
d.append(875)
print(c, d)
print(c is d)