print('OOOOOOOOOOOOOOOOOOOO')
print('O                  O')
print('O                  O')
print('O                  O')
print('O                  O')
print('O                  O')
print('O                  O')
print('O                  O')
print('O                  O')
print('OOOOOOOOOOOOOOOOOOOO')

print()


simbolo = 'O'
quantidade = 25

x = quantidade * simbolo

for f in range(int(len(x)/2)):
    if f == 0 or f == int(len(x)/2)-1:
        print(x)
    else:
        print(x[0]," "*(len(x)-4),x[-1])

print()


simbolo = '♥'
quantidade = 30

x = quantidade * simbolo

for f in range(int(len(x)/2)):
    if f == 0 or f == int(len(x)/2)-1:
        print(x[:int(len(x)/2)])
    else:
        print(x[0]," "*(len(x)-4),x[-1])