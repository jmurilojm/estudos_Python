#LER-ARQUIVOS

#Desta forma tem que mandar fechar:
	
doc = open('model.txt')#abrindo o arquivo
print(doc.read())
doc.close()#fechando o arquivo

print()
print(60*'-')
print()

#Desta forma fecha automaticamente:

documento = []
#a = ''
with open('model.txt') as doc2:
	#print(doc2.read())#Leitura completa
	#print(doc2.readline())#Leitura de linha
	#print(doc2.readlines())#Tufo em uma Lista
	documento.append(doc2.readlines())
	#a = doc2.readlines()

print()
print('Lista da lista: ',documento)
#print(' > ',a)
print()

print()
print(60*'-')
print()

tot = 0
for i in documento[0]:
	if i == '\n':
		continue
	else:
		print(' > ',i)
		
print('\n',tot)