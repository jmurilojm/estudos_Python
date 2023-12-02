import math

'''
Exemplo de valores considerando 300 ppi:
	
1cm = 118
2cm = 236
3cm = 354
4cm = 472
5cm = 591
6cm = 709
7cm = 827
8cm = 945
9cm = 1063
10cm  = 1181


Como achar os pixels por centímetro?
	
1 pol = 2.54 cm
Desejando 300 ppi por pol
Calcula-se 300 / 2.54 = 118.11023622047244
Então, cada 1cm = 118.11023622047244
'''

def Pixel():
	largura = float(input('Largura: '))
	comprimento = float(input('Comprimento: '))
	
	PPI = 3000
	POL = 2.54
	PX = PPI / POL
	
	larg = round(largura * PX)
	comp = round(comprimento * PX)
	
	print('\n> Dimensão em Pixel = ' , larg, ' x ', comp)
	
	#outra forma
	larg2 = round(largura * PPI / POL)
	comp2 = round(comprimento * PPI / POL)
	
	print('\n> Dimensão em Pixel = ' , larg2, ' x ', comp2)
	
	
Pixel()