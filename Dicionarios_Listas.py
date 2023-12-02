nome = 'paralelepipedo'

a = nome.capitalize()
print(a)

b = nome.center(20,'•')
print(b)

c = nome.count('P')
print(c)

d = {}

d['Autor'] = 'Murilo'
d['Ano'] = 2021
d['Cidade'] = 'Monteiro-PB'

print(d)

for x in d.keys():
	print(d[x])

print()

qtd = 6
nomes = []
for nome in range(qtd):
	nomes.append(input('Digite nome: '))

print(nomes)

#soma = 0
res = False
cont = 1

for x in range(len(nomes)):
	print((x+1),nomes[x])
	#soma += x
	if x == 'murilo':
		res = True
	
#media = soma / qtd
#print(f'Media: {media}')
print(res)

print(len(d))
print(len(nomes))
print(nomes[2])
print(nomes[2:5])

nomes[3] = 'Murilo'

print(nomes)

[a,b,c,d,e,f] = nomes

print(a,c,e)

