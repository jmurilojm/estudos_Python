cesta=[]
total=0

valor=True

while valor != 0:
	
	valor=float(input('> '))
	
	if valor > 0:
		cesta.append(valor)
		total+=valor
	elif valor == -1:
		total-=cesta.pop()
	
print('\n Finalizado!\n')

print(cesta)
print()
print(f'>>> Total a pagar = R$ {total:.2f}')