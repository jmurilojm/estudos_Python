from random import randint

def linha():
    print('========================================')


class Pessoa:
    __nome = ''
    
    def getNome(self):
        return self.__nome
        
    def setNome(self,nome):
        self.__nome = nome.title()


class Banco():
    __nome = 'Cliente BANCO DO BRASIL S/A'
    
    def getNome(self):
        return self.__nome


class Cliente(Pessoa):
    
    __saldo = 0.0
    __numero = 0
    __historico = []
    
    banco = Banco()
    
    def infor(self):
        linha()
        print(self.banco.getNome())
        print(f'Nome: {self.getNome()}')
        print(f'Conta: {self.__numero}')
        print(f'Saldo: R$ {self.__saldo :.2f}')
        linha()
        print()
        
    def setSaldo(self,valor):
        self.__saldo = valor
        
    def setNumero(self):
        self.__numero = randint(1111,1999)
        
    def sacar(self,valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            linha()
            print(self.banco.getNome())
            print(f'Nome: {self.getNome()}')
            print(f'Conta: {self.__numero}')
            print(f'Saldo: R$ {self.__saldo :.2f}')
            print()
            print(' > Saque realizado com sucesso.')
            print(f' > R$ -{valor :.2f}')
            print()
            print(f'Saldo: R$ {self.__saldo :.2f}')
            linha()
            print()
            self.__historico.append(f'• Saque R$ {valor}')
            
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            linha()
            print(self.banco.getNome())
            print(f'Nome: {self.getNome()}')
            print(f'Conta: {self.__numero}')
            print(f'Saldo: R$ {self.__saldo :.2f}')
            print()
            print(' > Depósito realizado com sucesso.')
            print(f' > R$ {valor :.2f}')
            print()
            print(f'Saldo: R$ {self.__saldo :.2f}')
            linha()
            print()
            self.__historico.append(f'• Depósito R$ {valor :.2f}')

    def transferir(self,valor,conta):
        if valor <= self.__saldo:
            self.__saldo -= valor
            conta.__saldo += valor
            linha()
            print(self.banco.getNome())
            print(f'Nome: {self.getNome()}')
            print(f'Conta: {self.__numero}')
            print(f'Saldo: R$ {self.__saldo :.2f}')
            print()
            print(' > Tranferência realizada com sucesso.')
            print(f' > Valor:  R$ {valor :.2f} > Para: {conta.getNome()}')
            print()
            print(f'Saldo: R$ {self.__saldo :.2f}')
            linha()
            self.__historico.append(f'• Transferência R$ {valor} > {conta.getNome()} - {conta.__numero}')
            print()
        else:
             print(' > Saldo insuficiente. Tranferência não realizada.')
             print()
             
    def extrato(self):
        linha()
        print('            <<< EXTRATO >>>')
        linha()
        print(self.banco.getNome())
        print(f'Nome: {self.getNome()}')
        print(f'Conta: {self.__numero}')
        print()
        for h in self.__historico:
            print(h)
        print()
        print(f'Saldo: R$ {self.__saldo :.2f}')
        linha()
        print()
             



class Tela:
    c1 = Cliente()
    c1.setNome('Fulano de Tal')
    c1.setNumero()
    c1.setSaldo(800)
    c1.infor()
    
    c2 = Cliente();
    c2.setNome('Sicrano Sobrenome')
    c2.setNumero()
    c2.setSaldo(500)
    c2.infor()
    
    c1.transferir(255,c2)
    c1.sacar(.50)
    
    c1.infor()
    c2.infor()
    c1.extrato()
    
    c2.depositar(860)
    c2.extrato()
    c1.extrato()
    