# dicionarios.py

dados = {'nome': 'Fulano', 'peso': 85, 'altura': 1.65}

print(dados)
print(dados['nome'])

for dado in dados:
	print(dado)
	
for dado in dados.items():
	print(dado)
	
for chave_dado, valor_dado in dados.items():
	print(chave_dado,':',valor_dado)