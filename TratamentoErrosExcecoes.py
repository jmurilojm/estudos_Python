try:#tente...
	a=int(input('Numerador: '))
	b=int(input('Denominador: '))
	res=a/b
	
#except:#falhou! falha! se falhar...
#	print('\nFalha na opecao!')
	
except Exception as erro:#identificar onde
	print(f'\nProblema encontrado: {erro.__class__}')
	
else:#se tufo ok... / opcional
	print(f'{res:.2f}')
	
finally:#certo ou errado aparece / opcional
	print('\nVolte sempre!')

print()
print()	
#################################################

try:
	x = 8/y
	
except ZeroDivisionError: # excessao
	print('Denominador igual a zero. Nao pode!')
except NameError: # excessao
	print('Nao calcula-se com String!')
else: # tudo ok faca
	print('Sem erros! :-)')
	print(x)
finally: # exibira sempre
	print('Consulta realizada.')
	
print()
print()	
#################################################
	
n=-6

if n <= 0:
	raise ValueError('O número digitado é Negativo!')
	
print()
print()	
#################################################
	
class NumeroInvalidoError(Exception):
	pass
	
nota=6.9

if nota < 7:
	raise NumeroInvalidoError
else:
	print(f'Nota = {nota}')