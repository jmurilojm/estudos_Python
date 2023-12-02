#TRY-EXCEPT

try:
	a = 10
	b = v
	calc = a / b
except ZeroDivisionError:
	print('Nao e permitida a divisao por 0(zero)')
#print(10/0)
except TypeError:
	print('Apenas numeros!')
except NameError:
	print('Tipo errado')
else:
	print('Executada sem erros')
	print(calc)
finally:
	print('Fim! (rodape)')