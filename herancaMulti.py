class Pessoa:
	nome = None
	idade = 0
	endereco = None
	cpf = 0
	sexo = None
	
	def infor(self):
		print(self.nome)
		print(self.idade)
		print(self.endereco)
		print(self.cpf)
		print(self.sexo)
		print('= = = = = = = = = = = = = = = =')
	
class Pai(Pessoa):
	filhos = None
	esposa = None
	
	def infor_pai(self):
		print(self.filhos)
		print(self.esposa)
	
class Mae(Pessoa):
	filhos = None
	esposo = None
	
	def infor_mae(self):
		print(self.filhos)
		print(self.esposo)
	
class Filho(Pessoa):
	pai = None
	mae = None
	
	def infor_filho(self):
		print(self.pai)
		print(self.mae)
	
	
#================================================

pai = Pai()
pai.nome = 'Murilo'
pai.infor()

mae = Mae()
mae.nome = 'Jessica'
mae.infor()

filho = Filho()
filho.nome = 'Douglas'
filho.infor()