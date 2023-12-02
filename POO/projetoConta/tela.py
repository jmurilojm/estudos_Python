from conta import Conta

p1=Conta()
p2=Conta()

p1.setNome('Murilo Lopes')
p1.setIdade(34)

p2.setNome('Jessica Poliana')
p2.setIdade(29)

p1.infor()
p2.infor()

print(dir(p1))
print()

print(p1)
print(p2)