from aluno import Aluno
from pessoa import Pessoa
from sala import Sala



sala1 = Sala(9,'A')
sala2 = Sala(8,'B')

aluno1 = Aluno('Programando',23,'456-7',sala1)
aluno2 = Aluno('Python',56,'789-0',sala2)


sala1.add_aluno(aluno1)
sala2.add_aluno(aluno2)

aluno1.infor()
aluno2.infor()

sala1.listar_alunos()
sala2.listar_alunos()