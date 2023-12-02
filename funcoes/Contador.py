def caracteres(informe_texto):
    total_caracteres = 0
    
    for letra in informe_texto:
    	total_caracteres += 1
    	if letra == ' ':
    		total_caracteres -= 1
    		continue
    return total_caracteres
    pass
	
	

if __name__ == '__main__':
    # Exemplo de uso:
    texto = caracteres('Programando em Python')

    print(texto)