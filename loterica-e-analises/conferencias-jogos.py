from jogos import AnaliseMegaSena as AMS
from jogos import AnaliseIntuitivaMegaSena as AIMS
from jogos import AnaliseLotofacil as ALF
from jogos import AnaliseLotomania as ALM
from jogos import AnaliseDiaDeSorte as ADS
from jogos import AnaliseMaisMilionaria as MM
from jogos import AnaliseMaisMilionariaTrevo as MMT

#==========CONFERENCIAS=============
'''
Dias:
	Seg: Lotofacil, Lotomania
	Ter: Lotofacil, Dia de Sorte
	Qua: Lotofacil, MegaSena, Lotomania
	Qui: Lotofacil, Dia de Sorte
	Sex: Lotofacil, Lotomania
	Sab: Lotofacil, MegaSena, Dia de Sorte

Valores:
	MegaSena = 5,50
	Lotofacil = 2,50
	Lotomania = 2,50
	Dia de Sorte = 3,00
	
Acertos:
	MegaSena:
		4, 5, ou 6 em 6 de 60
	Lotofacil: 
		11, 12, 13, 14 ou 15 em 15 de 25
	Lotomania: 
		15, 16, 17, 18, 19 ou 20 em 50 de 100
	Dia de Sorte: 
		4, 5, 6 ou 7 em 7 de 31
'''

#============MEGASENA===============
jm1 = [2,10,33,43,25,17]#alexs
jm2 = [10,20,25,33,34,48]
jm3 = [2,10,25,33,48,53]
jm4 = [2,10, 20, 25, 33, 34]#ops

sf1 = [4,5,17,20,48,52]#sorteios de fevereiro
sf2 = [19,22,37,44,51,56]
sf3 = [6,12,32,44,51,57]
sf4 = [5,9,14,30,38,50]
sf5 = [7,8,14,19,32,45]

#para sabado 18.02.23
pafev = [5,14,19,32,44,51]#jogueiNoApp
pafev2 = [9,14,19,32,44,51]#noGrupo

#jogos de 18.02
jo1 = [3,11,15,24,19,55]
jo2 = [3,11,15,24,19,55]
jo3 = [25,58,44,32,56,51]
jo4 = [21,23,10,18,15,17]
jo5 = [15,3,17,13,28,39]
jo6 = [4,6,21,55,34,27]
jo7 = [9,18,20,34,50,52]
jo8 = [2,12,19,25,38,46]##
jo9 = [2,5,12,13,19,24]
jo10 = [2,10,33,43,25,17]#
jo11 = [9,14,19,32,44,51]
jo12 = [1,5,7,39,40,60]
jo13 = [6,22,37,40,52,58]

ppt = [5,9,11,14,22,32,38,44,45,51]

#jogos 01.03
p1= [2 , 6 , 17 , 40 , 44 , 53]
p2= [27 , 3 , 40 , 18 , 11 , 19]
p3= [2 , 10 , 33 , 43 , 25 , 17]
p4= [7 , 11 , 15 , 18 , 24 , 29]
p5= [1 , 3 , 5 , 39 , 49 , 60]
p6= [13 , 15 , 26 , 28 , 48 , 45]
p7= [17 ,  20 , 22 , 35 , 41 , 42]
p8= [3 , 12 , 17 , 20 , 35 , 40]
p9= [2 , 13 , 25 , 38 , 43 , 57]
p10= [11 , 14 , 25 , 32 , 38 , 45]

k = [6,7,18,26,50,49,35,22,32,37]#49,35,22,32,37
k2 = [7, 18, 22, 26, 35, 49]#para 16.03
#sorteados 12, 17, 43, 44, 48, 60

AMS(k)#Chamada de Funcao
#AIMS()#Chamada de Funcao



#============LOTOFACIL===============
jm11 = [2,8,5,3,23,25,17,16,13,11,10,19,22,21,6]
#ALF(jm11)#Chamada de Funcao



#============LOTOMANIA==============
a = [1,3,5,7,9,11,13,15,17,19,20,22,23,26,28,32,35,37,38,39,42,43,45,46,48,49,51,52,54,56,58,60,66,67,69,70,71,72,73,78,82,84,86,89,91,93,95,97,98,00]#13

original=[2,7,10,13,14,19,20,22,23,26,28,29,32,33,35,36,38,40,41,43,48,49,50,53,56,57,60,62,64,66,67,69,71,72,76,77,80,81,82,84,85,86,88,90,92,94,95,97,99,00]#13 14 15

jogada = [2,7,10,13,14,19,18,22,24,26,30,29,32,33,35,36,39,40,41,43,48,49,50,53,56,57,60,62,64,63,67,69,71,72,78,77,80,81,82,84,85,86,88,90,92,94,95,97,99,00]

#5,45,89-20,23,28,38,66,76
#20-18, 23-24, 28-30, 38-39, 66-63, 76-78

jogada2 = [2,7,10,13,14,19,18,22,24,26,30,29,32,33,35,36,39,40,41,43,48,49,50,53,56,57,60,62,64,61,67,69,71,72,78,77,80,81,82,84,85,86,88,90,92,94,95,97,99,00]
#66-61 66-65

#ALM(jogada2)#Chamada de Funcao



#============DIA_DE_SORTE============
a = [4,20,31,17,1,22,27]
b = [31,17,1,22,27,4]
c = [31,20,2]

#ADS(c)#Chamada de Funcao

#===========MAIS_MILIONARIA==========

jogo = [16,2,3,8]
#trevo = [2,3]

#3,6,16,31,39,46,48,50

#jogo = [16,46,48]
#trevo = [2,5]

#MM(jogo)
#MMT(trevo)