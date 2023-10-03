'''
Algorítmo para obter o cálculo do Índice de Massa Corporal - IMC.

É necessário que seja informado os valores de PESO e ALTURA nas variáveis "valorPeso" e "valorAltura".
'''

valorPeso = 85
valorAltura = 1.65

imc = valorPeso / (2 * valorAltura)

print('\nSeu IMC = {:.1f}\n'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
    if imc < 16.0:
        print('Magreza grave')
        print('\nAnorexia, bulimia, osteoporose e auto consumo de massa muscular.\n\nFonte: www.farmaciavitamed.com.br/noticias/indice-de-massa-corporal--imc--/54/166')
    elif imc >= 16.0 and imc < 17.0:
        print('Magreza moderada')
        print('\nTranstornos digestivos, debilidade, fadiga crónica, stress, ansiedade e difusão das hormonas.\n\nFonte: www.farmaciavitamed.com.br/noticias/indice-de-massa-corporal--imc--/54/166')
    elif imc >= 17.0 and imc < 18.5:
        print('Magreza leve')
        print('\nTranstornos digestivos, debilidade, fadiga crónica, stress, ansiedade e difusão das hormonas.\n\nFonte: www.farmaciavitamed.com.br/noticias/indice-de-massa-corporal--imc--/54/166')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso Normal')
    print('\nEstado normal, bom nível de energia, vitalidade e boa condição física. Mantenha o seu peso e IMC.\n\nFonte: www.farmaciavitamed.com.br/noticias/indice-de-massa-corporal--imc--/54/166')
elif imc >= 25.0 and imc <= 29.9:
    print('Sobrepeso')
    print('\nFadiga, problemas digestivos, problemas circulatórios, má circulação nas pernas e varizes.\n\nFonte: www.farmaciavitamed.com.br/noticias/indice-de-massa-corporal--imc--/54/166')
elif imc >= 30.0 and imc <= 34.9:
    print('Obesidade grau I')
    print('\nDiabetes, angina de peito, enfartes,trombo flebites, arteroscleroses, embolias, alterações menstruais.\n\nFonte: www.farmaciavitamed.com.br/noticias/indice-de-massa-corporal--imc--/54/166')
elif imc >= 35.0 and imc <= 39.9:
    print('Obesidade grau II (severa)')
    print('\nDiabetes, angina de peito, enfartes,trombo flebites, arteroscleroses, embolias, alterações menstruais.\n\nFonte: www.farmaciavitamed.com.br/noticias/indice-de-massa-corporal--imc--/54/166')
elif imc >= 40.0:
    print('Obesidade grau III (mórbida)')
    print('\nFalta de ar, apneia, sonolência, trombose pulmonar, úlceras varicosas, cancro do cólon, uterino e mamário, refluxo esofágico, discriminação social, laboral e sexual.\n\nFonte: www.farmaciavitamed.com.br/noticias/indice-de-massa-corporal--imc--/54/166')