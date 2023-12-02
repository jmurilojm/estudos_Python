class Conta:
	
	def __init__ (self):
		self.__nome = ''
		self.__idade = 0
		
	#Setters e Getters
	def setNome(self,nome):
		self.__nome = nome
		
	def getNome(self):
		return self.__nome
		
	def setIdade(self,idade):
		self.__idade = idade
		
	def getIdade(self):
		return self.__idade
		
	#Acoes
	def infor(self):
		print(f'Informacaoes de {self.__nome}: ')
		print(self.getNome())
		print(self.getIdade())
		print()
	
	def __str__ (self):
		txt = 'Nome: '+self.getNome()
		txt += '\nIdade: '+str(self.getIdade())
		txt += '\n'
		
		return txt
		

	pass