# tuplas.py

tupla = (3, 5, 1)
print(tupla)


#empacotar e desempacotar
#empacotando
tp = (7.60, 0.1, 5)

#desempacotando
(valor, taxa, meses) = tp
print(valor, taxa, meses)

#ignorando valor
valor2, taxa2, _ = tp
print(valor2, taxa2, _)

#ignorando multiplos
valor3, *resto2 = tp
print(valor3, *resto2)

valor4, *resto3, ultimo = tp
print(valor, *resto3, ultimo)