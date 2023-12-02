# var = lambda args : expressao

soma = lambda a, b : a + b
mult = lambda a, b, c : (a + b) * c

r_soma = soma(5, 7)
r_mult = mult(5, 7, 9)

print(r_soma)
print(r_mult)
print((lambda a, b : a * b) (5, 7))

r_subt = (lambda a, b : a - b) (5, 7)
print(r_subt)

