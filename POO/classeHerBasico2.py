class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    
class Sala():
    def __init__(self,ano,sigla):
        self.ano = ano
        self.sigla = sigla
        
        self.alunos = []
    def add_aluno(self,aluno):
        self.alunos.append(aluno)
        
    def infor(self):
        print(f'\nAlunos da sala: {self.ano}{self.sigla}:')
        [print(x.nome) for x in self.alunos]
    

class Aluno(Pessoa):
    def __init__(self,nome,idade,ra):
        Pessoa.__init__(self,nome,idade)
        self.ra = ra
        self.sala = Sala
        
    def add_sala(self,sala):
        self.sala = sala
        
    def infor(self):
        print(f'Dados do aluno {self.nome}: ',self.idade,self.ra,self.sala.ano,self.sala.sigla)
        
    
    
# ==================== TELA ====================

# ========== Instancias ==========
s1 = Sala(9,'A')
s2 = Sala(7,'B')

a = Aluno('Aluno 01',23,'123-4')
b = Aluno('Aluno 02',34,'567-8')

# ========== Atribuicoes ==========
s1.add_aluno(a)
s2.add_aluno(b)

a.add_sala(s1)
b.add_sala(s2)

# ========== Informacoes ==========
a.infor()
b.infor()

s1.infor()
s2.infor()