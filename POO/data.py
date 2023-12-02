class Data:
	def __init__(self,dia,mes,ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano
		pass
		
	
	def dataFormatada(self):
		return f'{self.dia}/{self.mes}/{self.ano}'