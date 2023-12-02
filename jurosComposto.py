'''
M = C (1 + i)**t

M - montante
C - capital
i - taxa (mes)
t - tempo (mes)

c = 1500
i = 10 / 100
t = 3

m = c*(1 + i)**t

print(f'{m:.2f}') #1.996,50
'''

c = float(input('Valor a emprestar: '))
i = int(input('Taxa: ')) / 100
t = int(input('Total de meses: '))

m = c * (1 + i) ** t

print(f'{m :.2f}')