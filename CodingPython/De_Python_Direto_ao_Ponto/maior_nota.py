# maior_nota.py

notas = [1, 6, 4, 10, 3, 2, 0, 7]

nota_maior = notas[0]
for nota in notas:
	if nota > nota_maior:
		nota_maior = nota
		
print(nota_maior,'ou',max(notas))