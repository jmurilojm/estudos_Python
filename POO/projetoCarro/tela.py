from carro import Carro
from motor import Motor

carro1 = Carro()
carro2 = Carro()

carro1.nome = 'Uno'
carro2.nome = 'Monza'

motor1 = Motor()

motor1.modelo = 'MKV'
motor1.potencia = 3500
carro1 = motor1


carro1.infor()
carro2.infor()
print(carro1.modelo)