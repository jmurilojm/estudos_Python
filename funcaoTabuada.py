def tabuada(valor):
    for x in range(10):
        print(f' {valor} + {x+1} = {(valor) + (x+1)}')
    print()
    for x in range(10):
        print(f' {valor} - {x+1} = {(valor) - (x+1)}')
    print()
    for x in range(10):
        print(f' {valor} x {x+1} = {(valor) * (x+1)}')
    print()
    for x in range(10):
        print(f' {valor} ÷ {x+1} = {(valor) / (x+1):.1f}')
    

numeroDesejado = 5


tabuada(numeroDesejado)