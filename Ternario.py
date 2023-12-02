l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
l3=[100,200,300,400,500]

for n1,n2,n3 in zip(l1,l2,l3):
	print(n1,n2,n3)
	
lista=[x*5 for x in range(1,11)]
print(lista)

nota = 8
print('Aprovado' if nota >= 7 else 'Reprovado')

numeros = [{1},{2},3]

[print(numero) for numero in numeros]
