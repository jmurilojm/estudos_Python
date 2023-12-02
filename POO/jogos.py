def pedra_papel_tesoura():
    import random as r
    '''
    O jogo consiste de 03 opções: Pedra, Papel e Tesoura.
    O jogador deve escolher apenas 01 das 03. Em seguida o computador também fará sua escolha e ambas serão comparadas para determinar o vencedor.
    Combinações para vencer em cada rodada:
        -Pedra quebra a Tesoura;
        -Papel enrola a Pedra;
        -Tesoura corta o Papel.
    '''
    
    # condicao para o loop
    time = True

    opcoes = ('PEDRA','PAPEL','TESOURA')
    
    # cabeçalho de apresntação
    print('''
====================================
           <<< JOGO >>>             
       PEDRA - PAPEL - TESOURA      
====================================

  Digite 0(zero) para sair do jogo.

            Boa Sorte!            

''')
    
    while time != False:
        '''
        O laço ficará executando até que o usuário digite o valor 0(zero).
        
        O laço está composto por:
            
            > escolha - recebe valor do usuário;
            > aposta - guarda a escolha em fonte maiscúla;
            > sorteio - guarda o valor gerado entre 0 e 2;
            > resultado - quarda a escolha que o computador fez nos itens da tupla Opcoes;
            > verificações;
            > Lançamento de resultados.
        '''
        escolha = input('> ')
        
        aposta = escolha.upper()
        sorteio = r.randint(0,len(opcoes)-1)
        resultado = opcoes[sorteio]
        # verifica e quadra a avaliação do valor que o usuário digitou.
        verificacao = True if aposta in opcoes else False
        
        
        if verificacao != True:
            # recebe o resultado da verificação
            if escolha == '0':
                # se 0(zero), finaliza.
                time = False
            else:
                # se não faz parte do jogo, faz o lançamento informando que o valor é inválido.
                print('\n   Valor digitado é inválido!\n')
        
        # comparando as apostas
        elif aposta == resultado:
            print(f'Computador: {resultado}')
            print('\n   Empatou!\n')
        elif aposta == 'PEDRA' and resultado == 'TESOURA':
            print(f'Computador: {resultado}')
            print('\n   Você venceu!\n')
        elif aposta == 'PAPEL' and resultado == 'PEDRA':
            print(f'Computador: {resultado}')
            print('\n   Você venceu!\n')
        elif aposta == 'TESOURA' and resultado == 'PAPEL':
            print(f'Computador: {resultado}')
            print('\n   Você venceu!\n')
        
        
        
        elif resultado == 'PEDRA' and aposta == 'TESOURA':
            print(f'Computador: {resultado}')
            print('\n   Que pena! Não foi dessa vez.\n')
        elif resultado == 'PAPEL' and aposta == 'PEDRA':
            print(f'Computador: {resultado}')
            print('\n   Que pena! Não foi dessa vez.\n')
        elif resultado == 'TESOURA' and aposta == 'PAPEL':
            print(f'Computador: {resultado}')
            print('\n   Que pena! Nao foi dessa vez.\n')
    print('\n   Jogo Finalizado!')
    pass





if __name__=='__main__':
    # exemplo de uso
    pedra_papel_tesoura()