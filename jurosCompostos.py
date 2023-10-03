valor = 3500
taxaJuros = 0.1
totalMeses = 3

for x in range(totalMeses):
    valor -= valor * taxaJuros


print(int(valor))