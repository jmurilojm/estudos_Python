palavra = 'paralelepipedo'.upper()


for letra in range(len(palavra)+1):
    print(palavra[0:letra])
    
for letra in range(len(palavra)):
    print(palavra[0:len(palavra)-1-letra])