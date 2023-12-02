'''
▻ Entrar com o valor da largura da garagem em metros.
▻ Entrar com o valor da profundidade da garagem em metros.
▻ Calcular área da garagem = largura da garagem * profundidade da garagem.
▻ Entrar com o valor da largura do terreno em metros.
▻ Entrar com o valor da profundidade do terreno em metros.
▻ Calcular área do terreno = largura do terreno * profundidade do terreno.
▻ Calcular percentual de ocupação = (área da garagem / área do terreno) * 100.
▻ Apresentar em tela o resultado.
'''

gLargura = 6
gComprimento = 17
gCalculo = gLargura * gComprimento

tLargura = 8
tComprimento = 23
tCalculo = tLargura * tComprimento

total = (gCalculo / tCalculo) * 100
print(f'{total:,.2f}')