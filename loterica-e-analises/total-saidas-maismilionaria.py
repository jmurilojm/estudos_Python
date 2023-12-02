from sorteios import MaisMilionaria as MM
from sorteios import MaisMilionariaTrevo as MMT

#LOTOFACIL

#TOTAL DE SAIDAS, POR NUMERO.

sorteios = MM()
sorteiosTrevo = MMT()

print('Sorteios = ',len(sorteios))
print()

quantidadeDeNumeros = 50
for i in range(1, quantidadeDeNumeros + 1):

	total_saidas = 0
	
	for x in sorteios:
		for numero in x:
			if numero == i:
				total_saidas += 1
				valor = numero
				
	print(f' {i} > {total_saidas}  {total_saidas * 100/len(sorteios):.0f}%')
	
print()
print()

quantidadeDeTrevos = 6
for i in range(1, quantidadeDeTrevos + 1):
	
	total_saidas = 0
	
	for x in sorteiosTrevo:
		for numero in x:
			if numero == i:
				total_saidas += 1
				valor = numero
				
	print(f' {i} > {total_saidas}  {total_saidas * 100/len(sorteiosTrevo):.0f}%')