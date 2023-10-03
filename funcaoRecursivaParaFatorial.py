def recursiva_fatorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * recursiva_fatorial(x - 1)
        

valorParaCalculo = 8

resultado = recursiva_fatorial(valorParaCalculo)


print(resultado)