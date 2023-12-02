from random import randint

palavras=['AGUIA','ARARA','AVESTRUZ','BOI','BORBOLETA','CABRA','CACHORRO','CANGURU','COBRA','CROCODILO','ELEFANTE','FOCA','GATO','GAVIAO','GIRAFA','HIPOPOTAMO','JAVALI','JACARE','LEAO','LOBO','LAGARTO','MACACO','OVELHA','PAVAO','PORCO','RATO','SAPO','TARTARUGA','TIGRE','TOURO','VACA']

aleatorio=randint(0,len(palavras))
palavra=palavras[aleatorio]
espacos=[]

for letra in palavra:
	espacos.append('_')

print('>>> DICA: é um ANIMAL! <<<')

for x in range(len(espacos)):
	print('   ',espacos[x],end='')
print('\n')

while '_' in espacos:
	
	chute=str(input('\nChute: ')).upper()
	if chute in palavra:
		#print(palavra.find(chute))
		posicao=palavra.find(chute)
		espacos[posicao]=chute
		print()
		for x in range(len(espacos)):
			print(' ',espacos[x],end='')
		print()

print('\n\nParabens!\n\nFinalizado!\n\n')