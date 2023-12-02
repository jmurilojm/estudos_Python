class Produto:
	def __init__(self,nome,preco,desconto):
		self.nome = nome
		self.preco = preco
		self.desconto = desconto
		pass
	    
	def precoComDesconto(self):
		return self.preco-self.preco*self.desconto
		pass
		
	def infor(self):
	    print(f'Nome: {self.nome}\nPreço: {self.preco}\nA pagar: {self.precoComDesconto()}\n')
	    pass