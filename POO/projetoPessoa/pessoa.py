class Pessoa:
	
	def __init__ (self,nome,idade,dataNascimento):
		
		self.no=nome
		self.id=idade
		self.daNa=dataNascimento
		
		
	def infor(self):
		inf = '= Dados e Informações ='
		print(inf)
		
		print(f'Nome:{self.no}\nIdade: {self.id} anos\nData de Nascimento: {self.daNa}\n')
		
pass

