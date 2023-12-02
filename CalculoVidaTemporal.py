from datetime import date

def cabecalho(titulo):
    print((len(titulo) + 4) * '=')
    print(f'  {titulo.upper()}')
    print((len(titulo) + 4) * '=')

def linha():
    print('====================================')


idade = 10

calculoMeses = idade * 12
calculoDias = idade * 365
calculoHoras = calculoDias * 24
calculoMinutos = calculoHoras * 60
calculoSegundos = calculoMinutos * 60

cabecalho('Cálculo - Vida temporal')
print(f'Horas: {calculoHoras}')
print(f'Minutos: {calculoMinutos}')
print(f'Segundos: {calculoSegundos}')
linha()

print(f'\nTotal de Horas: {calculoHoras}:{calculoMinutos}:{calculoSegundos} horas.')



