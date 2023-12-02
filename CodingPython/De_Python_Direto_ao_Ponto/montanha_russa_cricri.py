# montanha_russa_cricri.py

idade = 18
altura = 1.64
ticket_comprado = True

'''
if ticket_comprado == True:
	print('Ticket OK!')
elif idade >= 18:
	print('Idade permitida')
elif altura >= 1.65:
	print('Altura ideal')
else:
	print('Nenhum requisito foi satisfeito')
'''	

if ticket_comprado == True:
	print('Ticket OK')
	if idade >= 18 and altura >= 1.65:
		print('Passeio permitido')
	else:
		print('Nao autotizado')
		print('Idade ou altura abaixo do permitido')
else:
	print('Ticket invalido')