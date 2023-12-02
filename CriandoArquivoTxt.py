############### DOCUMENTACAO BASICA ############
'''
open() - abrir
close() - fechar
w - abreviacao de .write()
r - abreviacao de .read()
a - abreviacao de .append()

x = open('NomeDoArquivo','w') - criando
x.write('Escrevendo')

x = open('NomeDoArquivo','a') - abrir e adicionar
x.write('Adicionando')

x = open('NomeDoArquivo','r') - abrir e ler
x.read() - lendo

x.readline() - ler apenas uma linha

Para abrir um imagem no modo leitura usa 'b'
imagem = open('foto.jpg','rb')

'''

#criando Arquivo
arquivo = open('JMurilo.txt','w')#'w' escrever

#escrevendo
arquivo.write('Aqui é um teste.\n')
arquivo.write('Fazendo atraves do Pydroid 3.0')

#fechando - obrigatorio
arquivo.close()

#abrindo arquivo para leitura
arquivo = open('JMurilo.txt','r')#'r' leitura
print(arquivo.read())
arquivo.close()

arquivo = open('JMurilo.txt','r')
print(arquivo.readline())
arquivo.close()

#usando with nao e necessario close()
with open('JMurilo.txt','r') as arquivo:
	for linha in arquivo:
		print(linha)
		
#################################################

x = open('filosofos.txt')
print(x.read())
x.close()

print()

with open('filosofos.txt') as x:
	#com with nao presisa o close
	print(x.read())

# open('documento','modo')
#
# sem r - padrao ler
# r - read - ler
# w - write - escrever
# w+ - write plus - ler + escrever
# a - append - adicionar
# b - binary - binario

# rb - wb - ler ou escrever em modo binario

# read() - ler tudo
# read(size) - com quantidade de caracteres
# readline() - ler linha - uma por chamada
# readlines() - retorna as linhas em uma linha

# write(string) - palavra
# writelines(sequencia) - frases

print()

with open('filosofos.txt') as x:
	print(x.readlines())