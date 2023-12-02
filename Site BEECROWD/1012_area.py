'''
beecrowd | 1012
Área
Adaptado por Neilor Tonin, URI  Brasil

Timelimit: 1

>>>

Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
    
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

> Entrada

O arquivo de entrada contém três valores com um dígito após o ponto decimal.

> Saída

O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

> Exemplos de Entrada e Exemplo de Saída

3.0 4.0 5.2

TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000


12.7 10.4 15.2

TRIANGULO: 96.520
CIRCULO: 725.833
TRAPEZIO: 175.560
QUADRADO: 108.160
RETANGULO: 132.080
'''


def area_triangulo(base,altura):
    area = (base * altura) / 2
    print(f'TRIANGULO: {area:.3f}')
    
def area_circulo(raio):
    pi = 3.14159
    area = pi * (raio**2)
    print(f'CIRCULO: {area:.3f}')
    
def area_trapezio(base1,base2,altura):
    area = ((base1 + base2) * altura) / 2
    print(f'TRAPEZIO: {area:.3f}')
    
def area_quadrado(lado):
    area = lado**2
    print(f'QUADRADO: {area:.3f}')
    
def area_retangulo(lado1,lado2):
    area = lado1 * lado2
    print(f'RETANGULO: {area:.3f}')

A = float(input())
B = float(input())
C = float(input())

area_triangulo(A,C)
area_circulo(C)
area_trapezio(A,B,C)
area_quadrado(B)
area_retangulo(A,B)