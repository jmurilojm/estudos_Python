cesta=[]
total=0

valor=float(input('> '))

while valor != 0:
	if valor == -1:
		total-=cesta.pop()
	if valor > 0:
		cesta.append(valor)
		total+=valor
	valor=float(input('> '))
	
print('\n Finalizado!\n')

print(cesta)
print()
print(f'>>> Total a pagar = R$ {total:.2f}')