contas = []

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
    
def menu():
    print('''
    1 - Criar conta
    2 - Listar contas
    3 - Sair
    ''')
    opcao = int(input('Opcao: '))
    
    if opcao == 1:
        nome_conta = input('Nome da conta: ')
        nome_titular = input('Seu nome: ')
        numero = input('Numero para a conta: ')
        deposito = int(input('Valor inicial: '))
        
        nome_conta = criar_conta(nome_titular, numero, deposito)
        
        contas.append(nome_conta)
        print('Conta cadastrada com sucesso!')
        
        menu()
    
    elif opcao == 2:
        if len(contas) == 0:
            print('\nNenhuma conta foi aberta!')
            menu()
            
        else:
            [print(conta) for conta in contas]
            menu()
            
            
    elif opcao == 3:
        print('Fim')
        




menu()
