# IDENTIFICADOR DE LETRAS

cont=0

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0
H = 0
I = 0
J = 0
K = 0
L = 0
M = 0
N = 0
O = 0
P = 0
Q = 0
R = 0
S = 0
T = 0
U = 0
V = 0
W = 0
X = 0
Y = 0
Z = 0

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0

ç = 0

time = ''

print('==============================')
print('   IDENTIFICADOR DE LETRAS')
print('==============================')
print('\n  *PARA SAIR DIGITE > "sair"\n')

while time != 'sair':
	
	texto=input('> ')
	#texto = 'Programando em Python'
	
	if texto == 'sair':
		time = texto
	else:
		for letra in texto:
			cont+=1
			if letra == ' ':
				cont-=1
				continue
			
			elif letra == 'A':
				A+=1
			elif letra == 'B':
				B+=1
			elif letra == 'C':
				C+=1
			elif letra == 'D':
				D+=1
			elif letra == 'E':
				E+=1
			elif letra == 'F':
				F+=1
			elif letra == 'G':
				G+=1
			elif letra == 'H':
				H+=1
			elif letra == 'I':
				I+=1
			elif letra == 'J':
				J+=1
			elif letra == 'K':
				K+=1
			elif letra == 'L':
				I+=1
			elif letra == 'M':
				M+=1
			elif letra == 'N':
				N+=1
			elif letra == 'O':
				O+=1
			elif letra == 'P':
				P+=1
			elif letra == 'Q':
				Q+=1
			elif letra == 'R':
				R+=1
			elif letra == 'S':
				S+=1
			elif letra == 'T':
				T+=1
			elif letra == 'U':
				U+=1
			elif letra == 'V':
				V+=1
			elif letra == 'W':
				W+=1
			elif letra == 'X':
				X+=1
			elif letra == 'Y':
				Y+=1
			elif letra == 'Z':
				Z+=1
			
			elif letra == 'a':
				a+=1
			elif letra == 'b':
				b+=1
			elif letra == 'c':
				c+=1
			elif letra == 'd':
				d+=1
			elif letra == 'e':
				e+=1
			elif letra == 'f':
				f+=1
			elif letra == 'g':
				g+=1
			elif letra == 'h':
				h+=1
			elif letra == 'i':
				i+=1
			elif letra == 'j':
				j+=1
			elif letra == 'k':
				k+=1
			elif letra == 'l':
				l+=1
			elif letra == 'm':
				m+=1
			elif letra == 'n':
				n+=1
			elif letra == 'o':
				o+=1
			elif letra == 'p':
				p+=1
			elif letra == 'q':
				q+=1
			elif letra == 'r':
				r+=1
			elif letra == 's':
				s+=1
			elif letra == 't':
				t+=1
			elif letra == 'u':
				u+=1
			elif letra == 'v':
				v+=1
			elif letra == 'w':
				w+=1
			elif letra == 'x':
				x+=1
			elif letra == 'y':
				y+=1
			elif letra == 'z':
				z+=1
			
			elif letra == 'ç':
				ç+=1
		
	
print(f'\nTotal de caracteres: {cont}\n')

print(f'A = {A}     a = {a}')
print(f'B = {B}     b = {b}')
print(f'C = {C}     c = {c}     ç = {ç}')
print(f'D = {D}     d = {d}')
print(f'E = {E}     e = {e}')
print(f'F = {F}     f = {f}')
print(f'G = {G}     g = {g}')
print(f'H = {H}     h = {h}')
print(f'I = {I}     i = {i}')
print(f'J = {J}     j = {j}')
print(f'K = {K}     k = {k}')
print(f'L = {L}     l = {l}')
print(f'M = {M}     m = {m}')
print(f'N = {N}     n = {n}')
print(f'O = {O}     o = {o}')
print(f'P = {P}     p = {p}')
print(f'Q = {Q}     q = {q}')
print(f'R = {R}     r = {r}')
print(f'S = {S}     s = {s}')
print(f'T = {T}     t = {t}')
print(f'U = {U}     u = {u}')
print(f'V = {V}     v = {v}')
print(f'W = {W}     w = {w}')
print(f'X = {X}     x = {x}')
print(f'Y = {Y}     y = {y}')
print(f'Z = {Z}     z = {z}')