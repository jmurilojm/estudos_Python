'''
A cada vez que o programa for colocado em execução, você terá uma sequência de números para utilizá-los como palpite.
'''

from random import randint

palpiteGerado = []

for c in range(12):
    if len(palpiteGerado) == 6:
        break
    else: 
        n=randint(1,60)
    
    if n not in palpiteGerado:
        palpiteGerado.append(n)
        

print(sorted(palpiteGerado))