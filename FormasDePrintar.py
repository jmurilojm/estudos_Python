'''
@JMurilo _ j.murilo.87@gmail.com
'''

#================================================
#               FORMAS DE PRINTAR
#================================================

x = 12.2456

print(x)
print()

print('Valor = R$',x)

print(f'Valor = R$ {x}')

print(f'Valor = R$ {x : .1f}')

print('Valor = R$ %f' %x)

print('Valor = R$ %.1f' %x)

print(f'V {x:10} == {x:10f}')
print()

#================================================

y = f'Valor = R$ {x}'

print(y)

print(repr(y))
print()

#================================================

z = 'Murilo'

print(f'Jose {z} == {z !r}')
print('Jose {}'.format(z))
print('Jose {}'.format('Murilo'))
print('Jose {0} {1}'.format('Murilo','Lopes'))
print('Jose {1} {0}'.format('Murilo','Lopes'))

print('{nome} {sobrenome}'.format(nome = 'Jose Murilo', sobrenome = 'Lopes Ferreira'))



#Fim