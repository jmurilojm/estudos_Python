import os

arquivo = open('teste.txt') # abre
print(arquivo.read()) # ler
arquivo.close() # fecha



c = 0
with open('teste.txt') as arquivo: # abre
    for linha in arquivo: # ler
        if '2' in linha: # compara
            c += 1

print(c)



os.remove('teste.txt') # apaga o arquivo

with open('test.txt') as z: # abre
    print(z.read()) # ler