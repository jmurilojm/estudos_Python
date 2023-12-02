import datetime

class Pessoa:
    def __init__(self,nome,data_nasc,cpf):
        self.nome = nome
        self.dn = data_nasc
        self.cpf = cpf
        
class Historico:
    def __init__(self):
        self.data = datetime.datetime.today()
        self.transacoes = []
        
    def imprimir(self):
        print('\n> TRANSAÇÕES')
        [print(t) for t in self.transacoes]

class Conta:
    def __init__(self,cliente,numero,valor):
        self.titular = cliente
        self.conta = numero
        self.saldo = valor
        self.historico = Historico()
        print('Conta criada!')
        pass
        
    def sacar(self,valor):
        self.saldo -= valor
        self.historico.transacoes.append(f'Saque........: {valor} - {datetime.datetime.today()}')
        
    def depositar(self,valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Depósito.....: {valor} - {datetime.datetime.today()}')
        
    def extrato(self):
        self.historico.imprimir()
        print('\nSaldo........:',self.saldo)
        
    def infor(self):
        print('\nTitular...:',self.titular.nome)
        print('Data......:',self.historico.data)
        print('DN........:',self.titular.dn)
        print('CPF.......:',self.titular.cpf)
        print('Conta.....:',self.conta)
        print('Saldo.....:',self.saldo)
        
        
        
        
        
p1 = Pessoa('Linguagem','01/01/2022','123.456.789-00')

c1 = Conta(p1,'288-7',1500)
c1.infor()
c1.sacar(250)
c1.historico.imprimir()
c1.infor()
c1.depositar(1555)
c1.historico.imprimir()
c1.infor()

p2 = Pessoa('Python','31/12/2022','098.765.432-11')

c2 = Conta(p2,'249-1',1800)
c2.infor()
c2.historico.imprimir()
c1.extrato()