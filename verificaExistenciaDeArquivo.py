import os

name = 'jmurilo.txt'

if os.path.exists(name):
    #if exist the file in path, it will open.
    a = open(name,'r')
    print(a.read())
    a.close()
    
else:
    #else exist the file in path.
    print('Arquivo não existe!')
    
'''else:
    #else exist the file in path, it will created
    b = open(doc,'x')
    b.close()
    print('Arquivo criado')'''
    