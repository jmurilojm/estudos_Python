d=int(input('Dias: '))
h=int(input('Horas: '))
m=int(input('Minutos: '))
s=int(input('Segundos: '))

dS=d*24*60*60
hS=h*60*60
mS=m*60

print(f'\n>>> {dS+hS+mS+s} segundos')