#============SORTEIOS================
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

#============MEGA-SENA==============
def MegaSena():
	'''
	A aposta mínima, de 6 números, custa R$ 4,50.
	'''
	tabela = [
	['Nov', 1, 3, 24, 37, 51, 56],
	[9, 22, 27, 30, 33, 45],
	[12, 24, 26, 31, 37, 48],
	[6, 15, 19, 20, 33, 52],
	[1, 23, 32, 33, 36, 59],
	[2, 8, 28, 34, 41, 49],
	[10, 28, 45, 47, 57, 59],
	[12, 20, 22, 25, 26, 55],
	[2, 5, 27, 30, 46, 53],
	[25, 38, 45, 53, 55, 56],
	
	['Dez', 20, 23, 32, 36, 39, 57],
	[3, 23, 28, 34, 38, 48],
	[10, 25, 31, 37, 38, 57],
	[9, 15, 23, 25, 29, 30],
	[1, 6, 10, 30, 33, 35],
	[4, 5, 10, 34, 58, 59],
	
	['Jan', 1, 25, 29, 43, 46, 48],
	[5, 24, 25, 33, 38, 41],
	[13, 15, 53, 54, 55, 58],
	[19, 25, 43, 44, 48, 49],
	[3, 20, 45, 52, 53, 58],
	[2, 6, 10, 14, 34, 56],
	[3, 13, 16, 25, 27, 33],
	[2, 10, 18, 25, 34, 44],
	[9, 12, 20, 30, 32, 35],
	
	['Fev', 4, 5, 17, 20, 48, 52],
	[19, 22, 37, 44, 51, 56],
	[6, 12, 32, 44, 51, 57],
	[5, 9, 14, 30, 38, 50],
	[7, 8, 14, 19, 32, 45], 
	[9, 13, 25, 39, 46, 54], 
	[11, 23, 45, 53, 57, 59], 
	[10, 11, 19, 33, 58, 60], 
	[16, 22, 29, 35, 38, 49],
	
	['Mar', 6, 7, 25, 28, 31, 52],
	[8, 18, 26, 27, 47, 50],
	[9, 18, 33, 38, 41, 51],
	[3, 7, 15, 22, 24, 50],
	[6, 26, 32, 35, 37, 49],
	[12, 17, 43, 44, 48, 60],
	[4, 12, 14, 41, 46, 53]]
	#18.03.2023 - Qua,Sab
	return tabela
	
	
#=============LOTOFACIL==============
def Lotofacil():
	'''
	Você marca entre 15 e 20 números, dentre os 25 disponíveis no volante, e fatura prêmio se acertar 11, 12, 13, 14 ou 15 números.
	A aposta mínima, de 15 números, custa R$ 2,50.
	'''
	tabela = [
	['Jan',2,5,7,8,9,10,11,12,13,16,18,19,20,21,23],
	[2,3,4,7,8,9,14,16,17,18,19,20,22,24,25], 
	[1,3,4,7,8,9,10,11,12,13,15,18,21,22,25], 
	[1,2,4,5,8,9,10,11,14,15,16,17,18,21,25], 
	[1,2,3,5,6,13,14,16,18,19,21,22,23,24,25], 
	[1,2,3,5,9,10,11,12,13,19,21,22,23,24,25], 
	[1,2,3,4,7,10,11,12,13,14,16,17,20,24,25], 
	[1,3,4,8,11,12,15,16,18,19,20,22,23,24,25], 
	[2,3,8,11,12,13,16,17,18,19,20,22,23,24,25], 
	[2,3,5,6,7,8,9,12,15,18,19,20,21,22,24], 
	[2,3,5,6,8,9,11,13,16,17,18,21,23,24,25], 
	[2,4,6,7,11,12,13,14,15,17,18,19,22,23,25], 
	[1,4,6,8,9,10,13,14,15,17,18,19,20,21,24], 
	[2,3,4,5,9,10,11,14,15,16,17,20,21,22,24], 
	[1,2,3,4,6,7,8,12,15,19,20,21,22,23,25], 
	[1,4,5,6,8,10,11,13,14,15,17,19,22,23,24],
	[1,4,5,6,7,8,9,11,13,15,17,19,21,22,23],
	[1,3,5,8,10,11,12,13,14,16,18,19,20,21,25],
	[1,2,3,4,5,6,8,12,18,20,21,22,23,24,25],
	[1,2,3,6,7,8,10,12,15,17,20,21,22,23,24],
	[1,3,5,6,8,12,13,14,17,19,20,21,22,24,25],
	[1,2,4,5,7,8,9,10,11,12,14,17,22,23,24],
	[2,5,6,8,9,10,11,14,16,17,18,19,20,21,23],
	[2,3,4,8,9,10,11,12,13,16,17,18,19,20,23],
	[1,2,3,4,5,9,10,11,13,14,16,17,18,20,22],
	
	['Fev',2,4,5,6,8,9,10,12,13,14,19,20,21,22,25],
	[2,4,7,10,11,13,14,15,16,19,20,21,23,24,25],
	[1,3,7,8,9,11,12,13,14,18,19,20,21,23,25],
	[2,3,5,6,8,10,12,15,16,18,19,20,21,24,25],
	[1,3,4,6,7,8,10,11,12,14,19,21,22,24,25],
	[1,3,5,6,8,10,11,12,14,15,17,18,21,22,23],
	[1,2,4,5,6,8,9,11,12,14,17,18,21,23,24],
	[1,3,6,8,11,12,14,15,17,18,19,20,21,23,25]]
	#09.02.2023 - Seg,Ter,Qua,Qui,Sex,Sab
	return tabela
	

#============LOTOMANIA==============
def Lotomania():
	'''
	A Lotomania é fácil de jogar e de ganhar: basta escolher 50 números e então concorrer a prêmios para acertos de 20, 19, 18, 17, 16, 15 ou nenhum número.
	O preço da aposta é único e custa apenas R$ 2,50.
	'''
	tabela = [
	['Jan',00,1,7,8,9,32,35,36,38,47,52,55,56,71,73,74,92,94,98,99],
	[6,11,13,16,19,24,26,37,42,46,47,53,58,70,85,87,88,93,94,99],
	[3,6,7,8,17,32,36,37,41,43,49,57,67,72,73,74,77,91,95,99],
	[2,7,11,27,32,39,47,60,61,62,64,69,70,71,74,81,87,91,94,95],
	[8,18,37,40,44,47,50,54,63,64,65,67,68,74,78,81,84,87,88,95],
	[2,10,14,15,21,31,39,46,51,52,55,60,61,64,65,80,81,85,86,92],
	[4,18,21,31,32,34,35,36,40,42,45,48,50,59,68,75,82,87,93,97],
	[6,16,29,35,41,44,46,52,57,62,63,79,84,85,87,88,91,93,94,96],
	[1,4,5,8,9,22,25,26,51,64,66,68,70,72,74,78,79,91,94,95],
	[4,11,22,24,27,32,34,37,49,57,64,69,70,71,76,77,86,93,95,97],
	[6,7,17,26,30,31,33,36,42,44,48,51,53,56,58,61,73,81,86,95],
	[2,6,7,11,12,15,20,21,24,29,32,34,35,39,54,59,60,78,84,88],
	[2,3,10,13,26,33,39,48,50,51,56,57,60,67,74,78,80,84,90,94],
	['Fev',13,14,19,23,34,35,36,42,43,49,58,63,67,68,77,82,92,95,97,98],
	[00,16,17,18,19,26,28,35,39,40,43,58,67,69,75,77,78,85,90,95],
	[1,16,17,22,24,29,34,39,42,48,50,51,64,69,73,75,77,81,89,96],
	[1,3,16,22,26,31,37,48,54,55,56,61,62,64,73,78,82,92,96,99]]
	#08.02.2023 - Seg,Qua,Sex
	return tabela
	

#===========DIA_DE_SORTE=============
def DiaDeSorte():
	'''
	Escolha de 7 a 15 números dentre os 31 disponíveis e mais 1 “Mês de Sorte”.
	Acertos: 4, 5, 6 ou 7.
	O valor da aposta mínima, de 7 números, é de R$ 3,00.
	'''
	tabela = [
	['Dez',2,6,22,25,29,30,31],
	[6,7,10,12,23,25,31],
	[2,9,12,15,27,29,31],
	[3,5,10,13,14,20,29],
	[8,9,11,12,23,25,28],
	[2,4,7,16,29,30,31],
	[6,7,12,23,26,28,31],
	[2,6,10,17,21,22,26],
	[1,5,9,19,20,24,29],
	[6,16,18,20,25,29,31],
	[4,11,14,17,18,19,31],
	[2,6,7,9,20,26,29],
	[6,8,10,11,18,20,22],
	[1,2,4,7,13,23,26],
	['Jan',4,7,14,18,20,25,26], 
	[1,4,7,11,16,20,24],
	[2,4,12,13,16,21,29],
	[5,7,9,12,13,22,23],
	[17,19,20,24,27,28,31],
	[1,15,19,22,23,30,31],
	[3,15,17,18,20,29,31],
	[1,4,7,9,20,25,31],
	[1,4,17,18,22,24,31],
	[5,6,11,17,21,26,27],
	[2,3,10,11,15,20,27],
	[2,4,6,8,12,13,22],
	[13,15,19,23,26,27,28],
	['Fev',1,8,17,18,22,27,31],
	[2,4,6,9,17,19,30],
	[6,8,19,20,21,23,24],
	[11,13,15,18,20,21,22]]
	#07.02.2023 - Ter,Qui,Sab
	return tabela
	
	
#==========MAIS_MILIONARIA===========
def MaisMilionaria():
	tabela = [['Mai',1,3,7,15,23,44],
	
	['Jun',13,16,35,41,42,47],[1,9,17,30,31,44],[6,23,25,33,34,47],[6,16,21,24,26,45],
	
	['Jul',1,19,22,32,39,45],[9,12,35,44,47,48],[1,4,5,16,38,50],[6,11,12,14,15,18],[4,6,10,42,47,48],
	
	['Ago',4,13,15,31,39,45],[6,20,24,26,31,50],[14,31,39,44,45,46],[12,13,42,46,48,49],
	
	['Set',3,35,37,39,41,50],[3,11,13,23,33,47],[3,17,25,46,48,50],[10,18,20,39,42,49],
	
	['Out',6,19,33,34,39,47],[4,8,10,11,22,25],[4,26,27,29,34,35],[5,22,28,46,47,48],[4,5,11,27,34,50],
	
	['Nov',22,29,31,32,36,45],[10,14,21,31,39,42],[5,12,26,31,34,50],[3,16,17,21,23,37],
	
	['Dez',2,7,29,40,41,50],[12,22,30,33,43,44],[2,24,31,39,46,47],[14,15,29,32,41,50],[12,23,30,36,45,46],
	
	['Jan', 1, 3, 6, 13, 21, 32],
[3, 6, 8, 36, 49, 50],[1, 2, 16, 28, 33, 42],[2, 8, 9, 15, 28, 32],

['Fev', 8, 16, 20, 25, 45, 46],[7, 14, 15, 16, 18, 23],[2, 3, 11, 16, 17, 46],[2, 12, 22, 30, 33, 48]]
#25.02 - Dias de sorteio
	return tabela
	
def MaisMilionariaTrevo():
	tabela = [['Mai', 2, 4],
	
	['Jun', 2, 6],[1, 4],[1,2],[2,5],
	
	['Jul',1,5],[1,5],[1,3],[3,4],[2,5],
	
	['Ago',2,4],[1,5],[1,2],[1,3],
	
	['Set',4,6],[2,5],[1,3],[3,4],
	
	['Out',3,5],[5,6],[5,6],[3,4],[1,5],
	
	['Nov',5,6],[3,6],[5,6],[1,4],
	
	['Dez',2,6],[2,5],[1,2],[3,5],[2,6],
	
	['Jan', 4, 5],[1, 6],[2, 4],[1, 4],
	
	['Fev', 3, 4],[2, 3],[2, 3],[2, 3]]
#25.02 - Dias de sorteio
	return tabela