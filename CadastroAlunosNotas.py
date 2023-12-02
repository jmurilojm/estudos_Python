alunos=[]
dados=[]

totAlunos=int(input('Quantidade de alunos: '))

for x in range(totAlunos):
	dados.append(input('\nNome: '))
	
	for x in range(4):
		dados.append(float(input(f'{x+1}ª Nota: ')))
		
	alunos.append(dados[:])
	dados.clear()
	

print()
for aluno in range(len(alunos)):
	print(alunos[aluno])