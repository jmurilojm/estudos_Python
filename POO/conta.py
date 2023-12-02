import datetime

##################HISTORICO#######################

class Historico:
	def __init__(self):
		self.data_abertura = datetime.datetime.today()
		self.transacoes = []
		
	def imprime(self):
		print(f'\nData de abertura >>> {self.data_abertura}')
		print('Transacoes: ')
		for t in self.transacoes:
			print('-',t)

###################CLIENTE########################

class Cliente:
	def __init__(self,nome,sobrenome,cpf):
		self.nome = nome
		self.sobrenome = sobrenome
		self.cpf = cpf
	pass

####################CONTA#########################

class Conta:
	def __init__(self,numero,cliente,saldo,limite=10000):
		self.numero = numero
		self.cliente = cliente #agregacao
		self.saldo = saldo
		self.limite = limite
		self.historico = Historico()
	pass
	
	def depositar(self,valor):
		self.saldo += valor
		self.historico.transacoes.append(f'Deposito de R$ {valor}')
		print('Deposito realizado!')
		print()
		return True
		
	def sacar(self,valor):
		if valor < self.saldo:
			self.saldo -= valor
			self.historico.transacoes.append(f'Saque de R$ {valor}')
			print('Saque realizado!')
			print()
			return True
		else:
			print('Saldo insuficiente!')
			print()
			return False
	
	def extrato(self):
		self.historico.transacoes.append('Pedido de Extrato')
		print(self.numero)
		print(self.cliente.nome,'',self.cliente.sobrenome)
		print(self.saldo)
		print()
		return True
		
	def transferir_para(self,conta,valor):
		if valor < self.saldo:
			self.saldo -= valor
			conta.saldo += valor
			self.historico.transacoes.append(f'Tranferencia de R$ {valor} para {conta.cliente.nome} {conta.cliente.sobrenome}: {conta.numero}')
			print('Tranferencia realizada!')
			print()
			return True
		else:
			print('Saldo insuficiente')
			print()
			return False
		
#print(dir(Conta))#outros metodos da class