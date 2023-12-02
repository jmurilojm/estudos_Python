#Aplicando as vantagem do Try Except para o tratamento de erros.
#Utilizado para informar algum erro que tem haver com sintaxe, tipos e atc.

x = 'valor de x - execucao normal'

try:
    print(x) #tente

except: #msn amigavel de erro
    print('msn erro amigavel')
    
#except NameError: #msn para um determinado erro
#    print('msn para um determinado erro')

else: #se tudo bem
    print('Else - se tudo bem')
    
finally: # sempre sera executado
    print('Finally - Sempre executado')
    
    
#Disparando uma Raise Exception
#Utilizado para tratar algo que esta fora dos parametros que sao exigidos pelo script criado.

'''
numero = -10

if numero < 0:
    raise Exception('Valor nao permitido!')
'''

'''
numero = 'Frase'

if not type(numero) is int:
    raise Exception('Aceito apenas numeros!')
    
else:
    print(numero)
'''