"""
▻ Entrar com o valor da largura da garagem em metros.
▻ Entrar com o valor da profundidade da garagem em metros.
▻ Calcular área da garagem = largura da garagem * profundidade da garagem.
▻ Entrar com o valor da largura do terreno em metros.
▻ Entrar com o valor da profundidade do terreno em metros.
▻ Calcular área do terreno = largura do terreno * profundidade do terreno.
▻ Calcular percentual de ocupação = (área da garagem / área do terreno) * 100.
▻ Apresentar em tela o resultado.
"""

gLargura = float(input("Largura da garagem: "))
gComprimento = float(input("Comprimento da garagem: "))
gCalculo = gLargura * gComprimento

tLargura = float(input("Largura do terreno: "))
tComprimento = float(input("Comprimento do terreno: "))
tCalculo = tLargura * tComprimento

total = (gCalculo / tCalculo) * 100


"""
Para a zona norte da cidade, o percentual máximo é de 25%;
Para as zonas leste e oeste da cidade, o percentual máximo é de 30%;
Para a zona sul, menos povoada, o percentual máximo é de 40%.
"""

zona = str(input("Qual a zona? "))

print(f"Localizado na zona: {zona}")
print(f"Percentual de ocupação: {total:,.2f}")

if zona == "n" and total <= 25:
    print("O projeto atende as regras de zoneamento para a zona n")
elif zona == "l" or zona == "o" and total <= 30:
    print("O projeto atende as regras de zoneamento para as zonas l e o")
elif zona == "s" and total <= 40:
    print("O projeto atende as regras de zoneamento para a zona s")
else:
    print("Revise os dados informados")