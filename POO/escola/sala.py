class Sala:
    def __init__(self,ano,sigla):
        self.__ano = ano
        self.__sigla = sigla
        
        self.__alunos = []
    def add_aluno(self,aluno):
        self.__alunos.append(aluno)
        
    def getAno(self):
        return self.__ano
        
    def getSigla(self):
        return self.__sigla
    
    def listar_alunos(self):
        print(f'\nAlunos da sala {self.__ano}{self.__sigla}:')
        [print(x.getNome(),x.getIdade(),x.getRa()) for x in self.__alunos]