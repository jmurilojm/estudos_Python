from pessoa import Pessoa
from sala import Sala


class Aluno(Pessoa,Sala):
    def __init__(self,nome,idade,ra,Sala):
        Pessoa.__init__(self,nome,idade)
        self.__ra = ra
        
        self.__sala = Sala
        
    def getRa(self):
        return self.__ra
        
    def infor(self):
        print('Aluno: ',self.getNome(),self.getIdade(),self.__ra,self.__sala.getAno(), self.__sala.getSigla())