numero = int(input('Número: '))
divisores = 0


for x in range(1,numero+1):
    if numero % x == 0:
        divisores += 1
        

if divisores <= 2:
    print('\nPrimo')
else:
    print('\nNÃO primo')