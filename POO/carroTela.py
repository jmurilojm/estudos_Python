from carro import Carro,Motor,Lanterna

c1 = Carro('Monza','Chevrolet',1998)
c2 = Carro('Civic','Honda',2003)
m1 = Motor()
m2 = Motor()

m1.modelo = 'DKV'
m2.modelo = 'Honda'

c1.motor = m1
c2.motor = m2

# ACOES

c2.ligar()
c1.ligar_lanterna()
c2.ligar_lanterna()

c1.infor()
c2.infor()
