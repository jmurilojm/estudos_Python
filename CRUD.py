#CRUD

#C - Create - Criar
lista = []
print(lista)
lista.append('Eu')
print(lista)

#R - Read - Ler
lista = ['Eu',35]
print(lista)
for i in lista:
    print(i)

#U - Update - Atualizar
lista = ['Eu',35]
lista[0] = 'Murilo'
print(lista)

#D - Delete - Apagar
lista = ['Eu',35]
del lista[0]
#lista.pop(0)
print(lista)