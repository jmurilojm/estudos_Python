#CLASSE PRINCIPAL
class TV:
	def __init__(self):
		self.marca = ''
		self.ano = 0
		self.tamanho = 0
	pass
	
	def infor(self):
		'''Lista as informacoes do objeto.'''
		print(self.marca)
		print(self.tamanho)
		print(self.ano)
	pass
	