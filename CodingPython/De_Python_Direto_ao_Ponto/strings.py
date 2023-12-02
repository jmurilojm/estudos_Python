# strings.py

#criacao de strings
print('Nomal')
print('"Com aspas nas aspas"')
print('Conteudo com:\n\tPular linha e tab.')
print(r'mantendo \n com "r"(raw string) ')
print('Agora \\n com "backslash"')


#concatenacao de strings
string = 'Exemplo'
print(string + string)
print(string * 5)


#casting com strings
numero = 30.5
print(numero, type(numero))

numero_string = str(numero)
numero_string_2 = numero_string
print(numero_string, type(numero_string))

string_float = float(numero_string)
print(string_float, type(string_float))

numero_2 = '30'
string_int = int(numero_2)
print(string_int, type(string_int))


#metodos para strings
frase = '    navegar e preciso    '

print(frase.upper())
print(frase.replace('navegar', 'programar'))
print(frase.strip())

#item.join(lista)
lista = ['Que', 'bom', 'esta', 'lendo!']

print(' '.join(lista))
print('_'.join(lista))

#lista.split()
texto = 'Programar e um desafio!'
cripto = 'Pythonxexmuitoxdivertido'

print(texto.split())
print(cripto.split('x'))


#fatiamento de strings
palavra = 'programacao'

print(palavra[0])
print(palavra[0 : 4])
print(palavra[7 :])
print(palavra[: 8])


#formatacao de strings
x = 'Valor'
y = 30

#interpolacao com %
print('O %s e %i' %(x, y))

#str.format()
print('O {} e {}'.format(x, y))
print('O {0} e {1}'.format(x, y))
print('O {1} e {0}'.format(x, y))
print('O {txt} e {0}'.format(x, txt = 'total'))

print('O {} de Pi = {: .2f}'.format(x, 3.14159))
print('A = {1:.3f} / B = {0:.2f}'.format(1.2345, 3.14159))

#f-string
print(f'O {x} e {y}')

