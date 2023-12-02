def separar(texto):
    fatiamento = list(texto)
    
    letras = 0
    numeros = 0
    espacos = 0
    
    for letra in fatiamento:
        if not letra.isdigit():
            if letra == ' ':
                espacos += 1
            else:
                letras += 1
        else:
            numeros += 1
            
    print(f'Letras: {letras} - Números: {numeros} - Espaços: {espacos}')
    pass
    
    

separar('Programando em Python - 2022')


