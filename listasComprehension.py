lista = [5,8,3,9,2,6]

[print(n) for n in lista]
print('\n')

[print(i,n) for i, n in enumerate(lista)]
print('\n')

x = [(i,n) for i,n in enumerate (lista)]

print(x)
print('\n')

[print(n) for n in range(100,121)]