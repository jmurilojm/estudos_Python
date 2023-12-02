# PRINVIPAL >>> CARRO
class Carro:
	def __init__(self,nome,modelo,ano):
		self.nome = nome
		self.modelo = modelo
		self.ano = ano
		self.ligado = False
		self.motor = Motor()
		self.lanterna = Lanterna()
	pass
	
	def infor(self):
		print(f'Nome: {self.nome}')
		print(f'Modelo: {self.modelo}')
		print(f'Ano: {self.ano}')
		print(f'Motor: {self.motor.modelo}')
		print(f'Potencia: {self.motor.potencia}')
		print(f'Status: {self.motor.ligado}')
		print(f'Lanterna: {self.lanterna.ligado}')
		print()
		
	def ligar(self):
		if self.motor.ligado == False:
			self.motor.ligado = 'Motor Ligado'
			
	def desligar(self):
		if self.motor.ligado == True:
			self.motor.ligado = 'Motor Desligado'
		
	def buzinar(self):
		print('Pibit! Pibit! Pibit!')
		
	def ligar_lanterna(self):
		if self.lanterna.ligado == False:
			self.lanterna.ligado = 'Lanterna Ligou'
			
	def desligar_lanterna(self):
		if self.lanterna.ligado == True:
			self.lanterna.ligado = 'Lanterna Desligou'
			
# CLASS MOTOR
class Motor:
	def __init__(self):
		self.modelo = ''
		self.potencia = 0
		self.ligado = False
		pass

# CLASS LANTERNA
class Lanterna:
	def __init__(self):
		self.ligado = False
		pass
		
