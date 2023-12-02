nome=str(input('Nome: ')).upper()

print(nome)

for l in range(len(nome)+1):
	print(nome[0:l])
	
for l in range(len(nome)):
	print(nome[0:len(nome)-(l+1)])