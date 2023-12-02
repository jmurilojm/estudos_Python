from random import randint

palpite=[]

for c in range(12):
	if len(palpite) == 6:
		break
	else: 
		n=randint(1,60)
	
	if n not in palpite:
		palpite.append(n)

print(sorted(palpite))