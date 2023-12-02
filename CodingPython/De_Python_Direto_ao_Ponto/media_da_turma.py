# media_da_turma.py

notas = [7.3, 8.1, 6.9, 7.6, 9.3, 7.7, 8.5, 6.4, 7.1]

soma_das_notas = 0
for nota in notas:
	soma_das_notas += nota
	
media_da_turma = soma_das_notas / len(notas)
	
print(soma_das_notas)
print(media_da_turma)