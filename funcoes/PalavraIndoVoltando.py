def palavra(texto):
    letras = texto
    
    for l in range(len(letras)+1):
        print(letras[0:l])
    for l in range(len(letras)):
    	print(letras[0:len(letras)-(l+1)])
    	pass
    	
    	
palavra('Programando em Python')