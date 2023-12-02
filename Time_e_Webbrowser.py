#IMPORTANDO BIBLIOTECAS

import webbrowser
import time

intervalos=2
cont=0
print('Iniciando...')

while cont < intervalos:
	time.sleep(5)
	webbrowser.open( 'https://youtu.be/F2rvndCJsoA' )
	cont += 1
	
print('Fim!')

#Fim