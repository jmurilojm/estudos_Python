texto=input('Digite ou cole um texto: ')

cont=0
for letra in texto:
	cont+=1
	if letra == ' ':
		cont-=1
		continue
	
print(f'\nTotal de caracteres: {cont}')