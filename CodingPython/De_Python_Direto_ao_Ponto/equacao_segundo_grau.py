# equacao_segundo_grau.py

def equacao_segundo_grau():
	a = int(input('Valor de a = '))
	b = int(input('Valor de b = '))
	c = int(input('Valor de c = '))
	
	# ax**2 + bx + c
	
	delta = b**2 - 4*a*c
	print('∆: ',delta)
	
	if delta >= 0:
		raiz_de_delta = int(delta ** (.5))
		print('Raiz de ∆: ',raiz_de_delta)
		
		x1 = float((- b + raiz_de_delta) / (2*a))
		print('X¹: ', x1)
		x2 = float((- b - raiz_de_delta) / (2*a))
		print('X²: ', x2)
	else:
		print('Delta Negativo!')
		

equacao_segundo_grau()