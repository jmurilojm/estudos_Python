class Pessoa:
    def __init__(self,nome):
        self.nome = nome
        pass
        
class Aluno(Pessoa):
    def __init__(self,ra):
        self.ra = ra
        pass
    
class Curso:
    def __init__(self,nome,cargaHoraria):
        self.nome = nome
        self.cargaHoraria = cargaHoraria
        pass
    
class Sala:
    def __init__(self,ano,sigla):
        self.ano = ano
        self.sigla = sigla
        pass