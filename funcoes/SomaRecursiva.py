def somaR(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return numero + somaR(numero - 1)
        pass
        
        
resultado = somaR(100)

print(resultado)