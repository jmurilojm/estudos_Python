def palpites(quantidadePalpites):
    from random import randint

    print()
    
    cont=0
    
    while cont<quantidadePalpites:
        palpite=[]

        for c in range(12):
            if len(palpite) == 6:
                break
            else: 
                numeroSorteado=randint(1,60)
    
            if numeroSorteado not in palpite:
                palpite.append(numeroSorteado)
                
        print(f'> {cont+1}  > {sorted(palpite)}')
        cont+=1
        #end
        

palpitesDesejados = 5

palpites(int(palpitesDesejados ))