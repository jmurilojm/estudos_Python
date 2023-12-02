class Produto:
	def __init__(self,nome,preco):
		self.__nome = nome
		self.__preco = float(preco)
		
	def desconto(self,desc):
		calculo = (self.__preco * desc) / 100
		self.__preco -= calculo
		print(f'Desconto: {desc}% ({calculo})')
		print(f'Pagar: R$ {self.__preco}')
		
	def infor(self):
		print(f'Produto: {self.__nome}')
		print(f'Preco: R$ {self.__preco}')

	# === Getters e Setters ===
	@property
	def nome(self):
		return self.__nome
	
	@property
	def preco(self):
		return self.__preco
	
	'''
	@nome.setter
	def nome(self,novo_nome):
		self.__nome = novo_nome
		
	@preco.setter
	def preco(self,novo_preco):
		self.__preco = novo_preco
	'''

#================================================

			
p = Produto('Sandalia',85)
#p.nome = 'JM' #Set
#p.preco = 3 #Set
#print(p.nome) # Get
#print(p.preco) #Get
p.infor()
p.desconto(15)

