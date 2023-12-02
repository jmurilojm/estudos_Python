import csv
import time
import os

pessoas = []

sair = False
cabecalho = ['id','nome', 'email']
opções = []

def salva_csv(dicionario, lista_cabecalho, arquivo):
    """Dicionario para CSV"""
    with open(arquivo, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=lista_cabecalho)
        writer.writeheader()
        writer.writerows(dicionario)

def le_csv(arquivo):
    """Le CSV e retorna uma lista com os dicionarios"""
    lista = []
    with open(arquivo, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            lista.append(dict(row))
    return lista

def exibe_os_registros():
    """Exibe na tela com formatação
    os dados registrados"""
    # o \t gera o espaçamento de um tab
    global pessoas
    
    print(f"id\t\tnome\t\temail")
    print("-"*20)
    for pessoa in pessoas:
        _id = pessoa['id']
        nome = pessoa['nome']
        email = pessoa ['email']
        print(f"{_id}\t{nome}\t\t{email}")
    print("-"*10+"\n")

def adicionar_registro(nome, email, lista):
    """Adionar nova pessoa a lista"""
    ultimo_indice = obter_ultimo_indice(lista)
    d = {'id': "%d" % time.time(), 'nome': nome, 'email':email}
    lista.append(d)

def obter_input():
    nome = input("nome:")
    email = input("email:")
    adicionar_registro(nome, email, pessoas)

def deletar():
    exibe_os_registros()
    _id = input("Digite o id do registro que quer apagar:")
    indice_para_deletar = -1
    for i, pessoa in enumerate(pessoas):
      if pessoa["id"] == _id:
        indice_para_deletar = i
    if indice_para_deletar == -1:
      print("Indice não encontradao")
      return
    pessoas.pop(indice_para_deletar)  
    print("Remoção bem sucedida")

def atualizar_registro():
    exibe_os_registros
    _id = input("Digite o id do registro que quer atualizar:")
    indice_para_alterar = -1
    for i, pessoa in enumerate(pessoas):
      if pessoa["id"] == _id:
        indice_para_alterar = i
    if indice_para_alterar == -1:
      print("Indice não encontradao")
      return
    j = indice_para_alterar
    #pessoas.pop(indice_para_deletar)
    print("Registro encontrado")
    nome = input("Novo nome:")
    email = input("Novo email")
    pessoas[j]["nome"] = nome
    pessoas[j]["email"] = email 
    print("Atualização concluída")

def limpa_tela():
  os.system('cls' if os.name == 'nt' else 'clear')


def menu():
  print("="*20)
  print("Menu".center(20))
  print("="*20+"\n")
  for i, opção in enumerate(opções):
    print(f"[{i}] - {opção[0]}")
  print()


def adiciona_opção(nome, função):
  opções.append([nome, função])
  

# lê os registros salvos, se ouver
try: 
    pessoas = le_csv("cadastro.csv")
except FileNotFoundError:
    print("cadastro.csv será gerado")

adiciona_opção("Sair", None)
adiciona_opção("Registrar", obter_input)
adiciona_opção("Exibir", exibe_os_registros)
adiciona_opção("Atualizar Registro", atualizar_registro)
adiciona_opção("Deletar Registro", deletar)

# loop do programa
while True:
    menu()
    resposta = int(input("Qual opção você quer?"))
    if resposta == 0:
      salva_csv(pessoas, cabecalho, 'cadastro.csv')
      limpa_tela()
      break
    limpa_tela()
    opções[int(resposta)][1]()