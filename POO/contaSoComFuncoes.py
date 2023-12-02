def criar_conta(titular, numero, valor):
    
    conta = {
    'Titular':titular,
    'Conta':numero,
    'Saldo':valor
    }
    
    return conta
    
    
def sacar(conta, valor):
    conta['Saldo'] -= valor
    
def depositar(conta, valor):
    conta['Saldo'] += valor
    
def transferir(conta_transferidora, conta_destino, valor):
    conta_transferidora['Saldo'] -= valor
    conta_destino['Saldo'] += valor
    
def saldo(conta):
    print(conta['Saldo'])
    
def infor(conta):
    print('Titular...........:',conta['Titular'])
    print('Conta.............:',conta['Conta'])
    print('Saldo.............:',conta['Saldo'])
    print('------------------------------------')
    


conta1 = criar_conta('JM', '288-7', 100000)
conta2 = criar_conta('JP', '249-1', 50000)

print(conta1)
print(conta2)

print(conta1['Conta'])
print(conta2['Conta'])

saldo(conta1)
saldo(conta2)

infor(conta1)
infor(conta2)

sacar(conta1, 30)
sacar(conta2, 15)

infor(conta1)
infor(conta2)

depositar(conta1, 35)
depositar(conta2, 20)

infor(conta1)
infor(conta2)

transferir(conta1, conta2, 255)

infor(conta1)
infor(conta2)