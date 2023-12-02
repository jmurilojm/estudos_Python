#LOOP WHILE

n=10
p=1

while n > 0:
	print(n, end=' ')
	n -= 1
print('Terminado!')

print(34*'_ ')

while p < 11:
	print(p, end=' ')
	p += 1
print('Fim!')

print(34*'_ ')

num=0

while num < 11:
	if num < 5:
		print(f'{num} é Menor que 5')
	elif num == 5:
		print(f'{num} é Igual')
	else:
		print(f'{num} é Maior que 5')
	num += 1
print('Acabou!')

#Fim