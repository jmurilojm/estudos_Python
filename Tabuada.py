numero=int(input('Número: '))

print()

for x in range(10):
	print(f' {numero} + {x+1} = {(numero) + (x+1)}')
print()
for x in range(10):
	print(f' {numero} - {x+1} = {(numero) - (x+1)}')
print()
for x in range(10):
	print(f' {numero} x {x+1} = {(numero) * (x+1)}')
print()
for x in range(10):
	print(f' {numero} ÷ {x+1} = {(numero) / (x+1):.1f}')