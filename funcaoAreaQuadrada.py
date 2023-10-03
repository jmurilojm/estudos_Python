'''
1 - A função resebe um valor através das variáveis que entrarão como parâmetros.

2 - A função retornará o valor calculado.

3 - O valor calculado será armazenado na variável "cálculo" e em seguida impresso na tela através da função ""print".
'''

def areaQuadrada(base,altura):
    return base*altura


valorBase = 45
valorAltura = 73

calculo = areaQuadrada(valorBase ,valorAltura )


print(f'Dimensão = {calculo :.1f} de área²')