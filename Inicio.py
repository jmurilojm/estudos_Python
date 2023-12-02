#VARIAVEL

meuNome='Jose Murilo' #String - Frase
meuSobrenome='Lopes Ferreira'
idade=34 #Int - Inteiro
altura=1.67 #Float - Fluruante
tenhoMoto=True
tenhoCarro=False

print('Me chamo:',meuNome, meuSobrenome)
print(f'Me chamo: {meuNome} {meuSobrenome}')
print(f'Tenho {idade} de idade')
print(f'Tenho {altura} de altura')
print(f'{tenhoMoto} moto')
print(f'{tenhoCarro} carro')
print()

#LISTA - ARRAY []

lista=[]

# .append( objeto )
print(lista)
lista.append('Murilo') #Adiciona no fim
print(lista)
lista.append('Jessica')
print(lista)
# .insert( posicao , objeto )
lista.insert(1,'Douglas') #Adiciona na posicao
print(lista)
lista.insert(0,'DanDan')
print(lista)
print()

listaDois=['Z','A','B','E','I','O','U','AO']

# .pop( posicao )
print(listaDois)
listaDois.pop(0) #Remove da primeira posicao
print(listaDois)
# .pop()
listaDois.pop() #Remove da ultima posição
print(listaDois)
# .remove( objeto )
listaDois.remove('B') #Remove o determinado
print(listaDois)
print()

#DICIONARIO {} / LISTA [CHAVE] = VALOR

livros={}

print(livros)
livros['Titulo']='Cursando Programação'
print(livros)
livros['Autor']='FERREIRA,José Murilo Lopes'
print(livros)

# .keys()
print(livros.keys()) #Mostra chaves
# .values()
print(livros.values()) #Mostra valores das chaves

dic={'Titulo':'Cursando Prigramacao','Ano':2021}
print(dic)
print()

#TUPLAS - Lista FIXA - Lista IMUTAVEL

tupla='Murilo','Jessica'
print(tupla)
print(type(tupla))
tuplaDois=('Danilo','Douglas') #() é opcional
print(tuplaDois)
print(type(tuplaDois))

#Apenas um elemento - VIRGULA OBRIGATORIA
tup='Murilo',
print(tup)
print(type(tup))
tupDois=('Jessica',)
print(tupDois)
print(type(tupDois))
print()

#PRINT

dia=28
mes=3
ano=1987
print('Me chamo '+meuNome +' '+ meuSobrenome)
#set=
print('Me chamo '+meuNome,meuSobrenome,sep=' ')
print(dia,mes,ano)
#set=
print(dia,mes,ano,sep='/') #Escolhendo separador

print('Me chamo %s %s' % (meuNome, meuSobrenome))
print('Tenho %d anos de idade' % idade)
print('Tenho %f de altura' % altura)
print()

#CONVERSAO

a=int('2021') #Str para Int
b=float('2021.2') #Str para Float
c=str(2022) #Numero para Str

print(type(a))
print(type(b))
print(type(c))

#Fim