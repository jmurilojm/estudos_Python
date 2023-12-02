import os

pasta = '../EstudandoPython'

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        print(os.path.join(diretorio, arquivo))