'''
Criar um programa que leia a notas 
de indeterminados alunos e ao digitar -1 
o programa seja finalizado mostrando a 
media das notas informadas.

Caso seja digitado um valor fora do 
intervalo de nota 0 a 10, informar que 
o valor e invalido.
'''
alunos = 0
notas = 0

op = 0

while op != -1:
	op = float(input('Nota: '))
	
	if op >= 0 and op <= 10:
		alunos += 1
		notas += op
	elif op == -1:
		break
	else:
		print('Digite uma nota valida')

media = notas/(alunos if alunos != 0 else 1)	
print()
print(f'Media de {alunos} = {media}')