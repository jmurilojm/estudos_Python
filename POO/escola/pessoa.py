class Pessoa:
    def __init__(self,nome,idade):
        self.__nome = nome
        self.__idade = idade
        
    def getNome(self):
        return self.__nome
        
    def getIdade(self):
        return self.__idade