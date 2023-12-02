lista = []

class Pessoa:
    def __init__(self,nome):
        self.nome = nome
        

def verificar():
    pass
    
    
def listar():
    if len(lista) != 0:
        for i in lista:
            print('Nome...:',i.nome)
    else:
        print('Não há cadastrados!')
        
        
def pesquisar():
    if len(lista) != 0:
        id = input('Digite o nome: ')
    
        for i in lista:
            if i.nome == id:
                print('Encontrado >',end=' ')
                print('Posicao...:',lista.index(i))
    else:
        print('Não há cadastrados!')
            
            
def deletar():
    if len(lista) != 0:
        id = input('Digite o nome: ')
    
        for i in lista:
            if i.nome == id:
               lista.remove(1)
               print('Apagado!')
    else:
        print('Não há cadastrados!')
            
            
def criar():
    time = True
    
    
    while time != False:
        p = input('Ref [0/Sair]...: ')
        if p == '0':
            break
        n = input('Nome...........: ')
    
        p = Pessoa(n)
    
        lista.append(p)
        
        
def menu():
    while True:
        opcao = int(input('''
1 - CADASTRAR
2 - LISTAR
3 - PESQUISAR
4 - APAGAR

0 - SAIR

> '''))
        if opcao == 0:
            break
        elif opcao == 1:
            criar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            pesquisar()
        elif opcao == 4:
            deletar()




menu()