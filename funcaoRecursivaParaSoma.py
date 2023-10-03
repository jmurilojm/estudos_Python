def recursiva_soma(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + recursiva_soma(x - 1)
        
        
numeroParaCalcular = 56
        
resultado = recursiva_soma(numeroParaCalcular)


print(resultado)