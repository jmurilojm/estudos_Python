def quadrado(simbolo,tamanho):
    x = tamanho * simbolo

    for f in range(int(len(x)/2)):
        if f == 0 or f == int(len(x)/2)-1:
            print(x)
        else:
            print(x[0]," "*(len(x)-4),x[-1])
            pass
            
            
quadrado('0',25)