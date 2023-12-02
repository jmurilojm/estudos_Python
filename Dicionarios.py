dic = {}
print(dic)
print(type(dic))

print()

d = {'um':'one','dois':'to','tres':'three'}
print(d)
print(d['dois'])
d['dois'] = 'two'
print(d['dois'])
print(d)

print()

d1 = d
print(d1)

d2 = d.copy()
print(d2)

print()

#obtem o Valor da Chave. Nao havendo retorna 0
print(d.get('tres',0))#Chave 'tres',Posicao 0

print()

print(d)
#remove pela Chave
d.pop('dois')
print(d)

#remove o ultimo Chave+Valor
d.popitem()
print(d)

