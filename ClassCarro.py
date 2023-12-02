class Carro():
	
	modelo=''
	cor=''
	ano=0
	
	def __init__ (self,modelo,cor,ano):
		self.modelo=modelo
		self.cor=cor
		self.ano=ano
		
	def ligar(self):
		print('Ligando...')
	def desligar(self):
		print('Desligando...')
	def infor(self):
		print(self.modelo,self.cor,self.ano)
		
'''
class Carro():
	modelo=''
	cor=''
	ano=0
	ligado=False
	
	
c1=Carro()

c1.modelo='Fiat'
c1.cor='Branca'
c1.ano=2021
c1.ligado=True


print('Modelo: ' + str(c1.modelo))
print('Cor: ' + str(c1.cor))
print('Ano: ' + str(c1.ano))

estado='Sim' if c1.ligado else 'Nao'
print('Ligado: ' + str(estado))
'''

c1=Carro('Volvo','Vermelho',2020)

print(c1.ano)
c1.infor()
