t=('Mur','Jes','Dan','Dou')#imutav
lista=[]#mutavel - conceitos: lista, filas, pilhas
dic={}#mutavel

#==============TUPLAS================
print(' ========== TUPLAS ==========')
print('Total elementos: ',len(t))#tamanho
print('Elementos: ',t)#mostrar tupla
print('No indice: ',t[2])#Busca por indice
print('Em ordem: ',sorted(t))#organiza
print('Contando: ',t.count('Dan'))#quant
print('Indice: ',t.index('Dan'))#indice
print('indice: ',t.index('Dou',1))#a partir
#del(tupla)#deletar tupla

print()

cont=1
for n in t:#cada elemento
	print(f'{cont}º - ',n)
	cont+=1

print()

for n in enumerate(t):
	print(n)#elemento e posicao
	
print()

for posicao, n in enumerate(t):
	print(posicao, n)#elemento e posicao

print()

#==============LISTAS=================
print(' ========== LISTAS ==========')
print('Lista: ',lista)
lista.append('Mur')#adicionando
lista.append('Jes')
lista.append('Dan')
lista.append('Dou')
print('ADICIONADOS à lista: ',lista)

lista[2]='Sobri'#substituindo
print('Substituindo: ',lista)

lista.count('Dou')#quantos tem na lista
print('Quantos na lista: ',lista)

print('Quem esta na posicao: ',lista[2])#quem?

lista.insert(0,'3')#add na posicao
print('ADD na posicao: ',lista)

#apagando elementos
del lista[0]#deletando pelo indice
print('DELETADO por indice: ',lista)
lista.pop(3)#padrao é retirar pelo ultimo
print('RETIRADO por indice: ',lista)
lista.remove('Jes')
print('REMOVIDO pelo nome: ',lista)

#ordenando a lista
print('Em ordem: ',sorted(lista))#na ordem
print('Inverte: ',lista.sort(reverse=True))

#outra forma de criar lista
exemplo=list(range(4,11))
print('Criando com list(range(4,11)): ',exemplo)

#tamanho da lista
print('Tamanho da lista: ',len(lista))

print()

#===========Lista em Lista==============
dados=[] #ou list()
pessoa=[] # ou list()
print('Lista Dados: ',dados)
print('Lista Pessoa: ',pessoa)
print()

pessoa.append('Mur')#adicionando
print(dados)
print(pessoa)
pessoa.append(34)
print(dados)
print(pessoa)
print()

dados.append(pessoa[:])#copia lista p/ lista
print(dados)
print(pessoa)
print()

print(dados[0])#mostrar pelas posicoes
print(dados[0][0])
print(dados[0][1])
print()

#adicionando outra listana lista ja criada
pessoa[0]='Jes'
pessoa[1]=30
dados.append(pessoa[:])
print(dados)
print()

#interacao para adicionar lista em lista
galera=[]
infor=[]
for x in range(4):
#	infor.append(str(input('Nome: ')))
#	infor.append(int(input('Idade: ')))
	infor.append(x+1)
	infor.append(x*9)
	galera.append(infor[:])#copia
	infor.clear()#limpa
print('Galera: ',galera)
print()

#verificar maior de idade
totalmaior = totalmenor = 0
for p in galera: #p = indice da lista global
	if p[1] >= 18:
		print(f'{p[0]} é Maior de idade.')
		totalmaior += 1
	else:
		print(f'{p[0]} é Menor de idade.')
		totalmenor += 1
print(f'Total maior = {totalmaior}')
print(f'Total menor = {totalmenor}')
print()



#============DICIONARIO===============
print(' ========== DICIONARIOS ==========')
dados={} #ou dic()
dados={'Nome':'JMur','Idade':34}
print(dados)
print(dados['Nome'])
print(dados['Idade'])
dados['Sexo']='M' # adicionar nova categoria
dados['Mês']='03'
print(dados)
del dados['Mês'] # deletar categoria
dados['Nome']='J Mur' #Alterar valor
print(dados)
print()

filme={'Filme':'Homem Aranha',
'Ano':2021,
'Subtitulo':'De volta pra casa'
}
print(filme)
print()

#valor - chave(keys) - item
print(filme.values()) # valor
print(filme.keys()) #chave
print(filme.items()) #itens - pega tudo!
print()

for k,v in filme.items():
	print(k,':',v)

#for k in filme.keys():
#for k in filme.values():
print()

#criar lista com dicionarios
brasil=[]

estado1={'Cidade':'Mon','UF':'PB'}
estado2={'Cidade':'Recife','UF':'PE'}
print('Dicionario: ',estado1)
print('Lista Brasil: ',brasil)
brasil.append(estado1)
brasil.append(estado2)
print('Lista Brasil: ',brasil)
print()

#copia para lista
estado=dict()
pais=list()

for x in range(2):
	estado['City']=str(input('Cidade: '))
	estado['Estado']=str(input('UF: '))
	pais.append(estado.copy())#copy dicionario
print(pais)
print()

for estado in pais:
	print(estado)
print()

for estado in pais: #for da lista
	for k, v in estado.items(): #for do dict
		print(k,'-',v)
print()

for estado in pais:
	for k in estado.values():
		print(k, end=' ')
	print()
print()