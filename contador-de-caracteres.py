a = str(input(' > '))

vogais = ['a','e','i','o','u','á','ã','à','â','é','ê','í','ó','ô','õ','ú']
consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
simbolos = 0

vog = 0
con = 0
sim = 0
num = 0

for x in a.lower():
	if x in vogais:
		vog += 1
	elif x in consoantes:
		con += 1
	elif x.isdigit():
		num += 1
	else:
		sim += 1
print(f'\n> Vogais..............{vog}\n> Consoantes..........{con}\n> Números.............{num}')