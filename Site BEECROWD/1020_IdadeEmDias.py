'''
beecrowd | 1020
Idade em Dias
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1

>>>

Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

> Entrada
O arquivo de entrada contém um valor inteiro.

> Saída
Imprima a saída conforme exemplo fornecido.

> Exemplo de Entrada e Exemplo de Saída

400

1 ano(s)
1 mes(es)
5 dia(s)

800

2 ano(s)
2 mes(es)
10 dia(s)

30

0 ano(s)
1 mes(es)
0 dia(s)
'''


time = int(input())

anos = 0
meses = 0
dias = 0

while time >= 365:
    time -= 365
    anos += 1

while time >= 30:
    time -= 30
    meses += 1

print(f'{anos} ano(s)')    
print(f'{meses} mes(es)')
print(f'{time} dia(s)')