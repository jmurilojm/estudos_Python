#CRIAR_ARQUIVO

def criar(criar_arquivo_nome):
	'''
	Esta funcao cria um novo arquivo com o nome repassado no como argumento.
	'''
	opcao = input('Criar? [s/n] ')
	if opcao == 's':
		with open(criar_arquivo_nome,'w') as new_arq:
			nome = []
	else:
		print('Fim')
	
def verificar(verificar_arquivo_nome):
	'''
	Esta funcao verifica a existencia do arquivo mencionado atrqves do argumento. Caso o arquivo nao exista, e chamada a funcao "criar()".
	'''
	try:
		with open(verificar_arquivo_nome) as arq:
			print(arq.read())
	except:
		print('Nao existe! Criamos um pra voce!')
		
		criar(verificar_arquivo_nome)
					


verificar('t.txt')