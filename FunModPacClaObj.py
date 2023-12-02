#==========FUNCOES==========

def soma(): #Sem parametro e Print
	print('Funcao SOMA Sem parametros')

def somaDois(x,y): #Com parametro e Return
	resultado = x+y
	return resultado
	#Ou pode ser: return x + y
	
def subDois(x,y): #Com paramentro e Print
	print(x-y)

soma()

r=somaDois(34,76)
print(r)

subDois(56,31)


#==========MODULOS==========

#Isso deveria estar salvo em arquivo separado
def media(a,b,c,d):
	return (a+b+c+d)/4

#Este modo pra chamar o Metodo acima citado
#import mediaEscolar
#x=mediaEscolar.media(5,8,7,9)

x=media(5,8,7,9)
print(x)

#==========PACOTES==========
#==========CLASSES==========
#==========OBJETOS==========