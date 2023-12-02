def linha():
	print('='*30)


m=[[1,25,354],[48,5875,6],[86987,8,89]]

linha()
for l in m:
	for i in l:
		print(i, end=' ')
	print()
linha()

print()

linha()
for l in range(0,3):
	for c in range(0,3):
		print(f'{m[l][c]:^8}', end=' ')
	print()
linha()

print()

linha()
for l in range(3):
	for c in range(3):
		print(f'{m[l][c]:>8}', end=' ')
	print()
linha()

print()

linha()
for l in range(len(m)):
	for c in range(len(m)):
		print(f'{m[l][c]:<8}',end=' ')
	print()
linha()