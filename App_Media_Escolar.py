#APP MEDIA ESCOLAR

import time

print('Iniciando Programa...')
time.sleep(2)
print()

nome=input('Nome: ').upper()
mat=input('Materia: ').upper()
print()

print('Digite suas notas:')
print()

n1=float(input('1º Bimestre: '))
n2=float(input('2º Bimestre: '))
n3=float(input('3º Bimestre: '))
n4=float(input('4º Bimestre: '))

media=(n1+n2+n3+n4)/4
print()

if media < 7.0:
	print(f'Aluno {nome}, voce foi REPROVADO. Sua media em {mat} foi {media}')
else:
	print('PARABENS!!!')
	print()
	print(f'Aluno {nome}, voce foi APROVADO. Sua media em {mat} foi {media}')
	
#Forma mais enxuta

'''
notas=[]

print(notas)

for x in range(1,5):
	notas.append(float(input('%dª nota:' %x)))

print(notas)

soma=0
for nota in notas:
	soma += nota

print('A media é ',soma/4)
'''

#Fim!