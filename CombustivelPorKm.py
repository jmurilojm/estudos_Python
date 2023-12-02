d=int(input('Distância em Km: '))
q=float(input('Km por litro: '))
v=float(input('Valor do Combustível: '))

print(f'\n>>> Litros = {d/q:.1f}\n>>> Valor = R$ {d/q*v:.2f}')