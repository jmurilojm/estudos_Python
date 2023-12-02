from produto import Produto

p1 = Produto('Note',1800,0.15)
#p1.nome = 'Note'
#p1.preco = 1800
#p1.desconto = 0.15

p2 = Produto('Cell',2100,0.35)
#p2.nome = 'Cell'
#p2.preco = 2100
#p2.desconto = 0.35

#pagar1 = p1.precoComDesconto()
#pagar2 = p2.precoComDesconto()


print(f'Nome: {p1.nome}\nPreço: {p1.preco}\nA pagar: {p1.precoComDesconto()}')
print()
print(f'Nome: {p2.nome}\nPreço: {p2.preco}\nA pagar: {p2.precoComDesconto()}')

print('\n==================================\n')



###############################################



p1 = Produto('Note',1800,0.15)
p1.infor()

p2 = Produto('Cell',2100,0.35)
p2.infor()