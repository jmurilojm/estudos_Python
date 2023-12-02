#Declarando Classe
class Pessoa():
        #Construtir de Classe __init__
        def __init__(self, nome, sexo, cpf):
        	self.__nome = nome
        	self.sexo = sexo
        	self.cpf = cpf
        	self.__ativo = true
        	
        #Metodo
        #__antes para tornar private
        def desativar(self):
        	self.__ativo = False
        	print("A pessoa foi desativada com sucesso")
        
        #getters e setters
        def get_nome(self):
        	return self.__nome
        	
        def set_nome(self, nome):
        	self.__nome = nome
        
        '''	
        #Novo metodo de get e set
        @property
        def nome(self):
        	return self.__nome
        
        @nome.setter
        def nome(self, nome):
        	self.__nome = nome
        '''

#Instaciamento
if __name__ == "__main__":
	pessoa1 = Pessoa("João", "M", "123456")
	
	print(pessoa1.nome)
	print(pessoa1.cpf)
	print(pessoa1.sexo)
	
	pessoa2 = Pessoa("Murilo","M","073770")
	
	print(pessoa2.nome)
	print(pessoa2.cpf)
	print(pessoa2.sexo)
	
	'''
	# Utilizando geters e setters
    pessoa1.set_nome("José")
    print(pessoa1.get_nome())

    # Utilizando properties
    pessoa1.nome = "José"
    print(pessoa1.nome)
    '''



