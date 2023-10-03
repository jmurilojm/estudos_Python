x='Fulano de Tal Beltrano'

#FATIAMENTO
print('=== FATIAMENTO ===')
print(x)#mostra tudo
print(x[10])#mostra letra do indice
print(x[2:15])#mostra letras do intervalo
print(x[2::])#mostra letras a partir do indice
print(x[0:15:2])#indice a indice, saltado
print(x[::2])#com intervalo saltado
print(x[1::2])#indice ao fim, intervalo saltado

print()

#ANALISE
print('=== ANALISE ===')
print('Total de letras = ',len(x))#tamanho
print('Total de "o" = ',x.count('o'))#quantos 'o'
print('Total de "o" em intervalo = ', x.count('o',5,15))
print(x.find('murilo'))#localizar. se sim = indice
print(x.find('o'))#localizar. se sim = indice 1º
print(x.find('joseph'))#localizar. se nao = -1
print('murilo' in x)#localizar. se sim = True

print()

#TRANSFORMACAO
print('=== TRANSFORMACAO ===')
print(x.replace('jose','joseph'))#troca
print(x.upper())#texto maiusculo
print(x.lower())#texto minusculo
print(x.title())#todas as 1as maiusculas
print(x.capitalize())#1ª maiuscula
print(x.strip())#remove espacos, inicio e fim
print(x.rstrip())#remove da direita - fim
print(x.lstrip())#remove da esquerda - inicio

print()

#DIVISAO
print(' === DIVISAO ===')
print(x.split())#corta nos espacos

print()

#JUNCAO
print(' === JUNCAO ===')
print('-'.join(x))#juntar com '-'
print(''.join(x))