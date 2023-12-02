def somar():
    numero_1 = int(input('1⁰ numero: '))
    numero_2 = int(input('2⁰ numero: '))
    
    return print(f'Resultado: {numero_1 + numero_2}')
    
def subtrair():
    numero_1 = int(input('1⁰ numero: '))
    numero_2 = int(input('2⁰ numero: '))
    
    return print(f'Resultado: {numero_1 - numero_2}')
    
def multiplicar():
    numero_1 = int(input('1⁰ numero: '))
    numero_2 = int(input('2⁰ numero: '))
    
    return print(f'Resultado: {numero_1 * numero_2}')
    
def dividir():
    numero_1 = int(input('1⁰ numero: '))
    numero_2 = int(input('2⁰ numero: '))
    
    if numero_2 == 0:
        return print(f'Resultado: 0')
    
    return print(f'Resultado: {numero_1 / numero_2}')

def menu():
    return print('''
    1 - SOMAR
    2 - SUBTRAIR
    3 - MULTIPLICAR
    4 - DIVIDIR
    
    0 - SAIR
    ''')
    
    
time = True
menu()

while time != False:
    opcao = int(input('> '))
    
    if opcao != 0:
        if opcao == 1:
            somar()
            menu()
        if opcao == 2:
            subtrair()
            menu()
        if opcao == 3:
            multiplicar()
            menu()
        if opcao == 4:
            dividir()
            menu()
    else:
        time = False
    
print('Fim')