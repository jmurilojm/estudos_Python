##### Possibilidade 01
'''
numero1 = '288-7'
titular1 = 'JMurilo'
saldo1 = 3000
limite1 = 10000

numero2 = '249-1'
titular2 = 'JPoliana'
saldo2 = 1500
limite2 = 10000
'''

##### Possibilidade 02
'''
conta1 = {'Numero':'288-7','Titular':'JMurilo','Saldo':3000,'Limite':10000}

conta2 = {'Numero':'249-1','Titular':'JPoliana','Saldo':1500,'Limite':10000}

print(conta1['numero'])
'''

##### Possibilidade 03
def cria_conta(numero,titular,saldo,limite):
	conta = {'Numero':numero,'Titular':titular,'Saldo':saldo,'Limite':limite}
	return conta
	
def depositar(valor,conta):
	conta['Saldo'] += valor
	
def sacar(valor,conta):
	conta['Ssldo'] -= valor
	
def extrato(conta):
	print('Titular da conta: {}\nSaldo: {}'.format(conta['Titular'],conta['Saldo']))
	
	
conta1 = cria_conta('288-7','JMurilo',3000,10000)
conta2 = cria_conta('249-1','JPoliana',1500,10000)
	
extrato(conta1)
depositar(550,conta1)
extrato(conta1)