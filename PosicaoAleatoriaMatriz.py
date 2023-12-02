import random

aleatorio=random.randint(1,33)
aleatorio2=random.randint(1,33)

for linha in range(1,34):
	for coluna in range(1,34):
		if linha == aleatorio and coluna == aleatorio2:
			print('  ',end='')
			continue
		print([] ,end='')
		
	print()
	
print()

print('Posicao: ',aleatorio,'x',aleatorio2)