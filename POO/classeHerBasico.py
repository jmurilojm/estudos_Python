class Pessoa():
    nome = None
    idade = None
    
    
class Sala():
    ano = None
    sigla = None
    
    alunos = []
    def add_aluno(self,aluno):
        self.alunos.append(aluno)
        
    def infor(self):
        print(f'\nAlunos da sala: {self.ano}{self.sigla}')
        [print(x.nome) for x in self.alunos]
    

class Aluno(Pessoa):
    ra = None
    
    sala = Sala
    def add_sala(self,sala):
        self.sala = sala
        
    def infor(self):
        print(f'Dados do aluno {self.nome}:',self.idade,self.ra,self.sala.ano,self.sala.sigla)
        
    
    
# ==================== TELA ====================

# ========== Instancias ==========
s = Sala()
s.ano = 9
s.sigla = 'A'

s2 = Sala()
s2.ano = 7
s2.sigla = 'B'

a = Aluno()
a.nome = 'Aluno 01'
a.idade = 23
a.ra = '123-4'

b = Aluno()
b.nome = 'Aluno 02'
b.idade = 34
b.ra = '567-8'

# ========== Atribuicoes ==========
s.add_aluno(a)
s2.add_aluno(b)

a.add_sala(s)
b.add_sala(s2)

# ========== Informacoes ==========
a.infor()
b.infor()

s.infor()
s2.infor()