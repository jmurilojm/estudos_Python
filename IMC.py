peso=float(input('Peso: '))
altura=float(input('Altura: '))

imc=peso/(2*altura)

print('\nSeu IMC = {:.1f}\n'.format(imc))

if imc < 18.5:
	print('Abaixo do peso')
	if imc < 16.0:
		print('Magreza grave')
		print('\nAnorexia, bulimia, osteoporose e auto consumo de massa muscular.')
	elif imc >= 16.0 and imc < 17.0:
		print('Magreza moderada')
		print('\nTranstornos digestivos, debilidade, fadiga crónica, stress, ansiedade e difusão das hormonas.')
	elif imc >= 17.0 and imc < 18.5:
		print('Magreza leve')
		print('\nTranstornos digestivos, debilidade, fadiga crónica, stress, ansiedade e difusão das hormonas.')
elif imc >= 18.5 and imc <= 24.9:
	print('Peso Normal')
	print('\nEstado normal, bom nível de energia, vitalidade e boa condição física. Mantenha o seu peso e IMC.')
elif imc >= 25.0 and imc <= 29.9:
	print('Sobrepeso')
	print('\nFadiga, problemas digestivos, problemas circulatórios, má circulação nas pernas e varizes.')
elif imc >= 30.0 and imc <= 34.9:
	print('Obesidade grau I')
	print('\nDiabetes, angina de peito, enfartes,trombo flebites, arteroscleroses, embolias, alterações menstruais.')
elif imc >= 35.0 and imc <= 39.9:
	print('Obesidade grau II (severa)')
	print('\nDiabetes, angina de peito, enfartes,trombo flebites, arteroscleroses, embolias, alterações menstruais.')
elif imc >= 40.0:
	print('Obesidade grau III (mórbida)')
	print('\nFalta de ar, apneia, sonolência, trombose pulmonar, úlceras varicosas, cancro do cólon, uterino e mamário, refluxo esofágico, discriminação social, laboral e sexual.')