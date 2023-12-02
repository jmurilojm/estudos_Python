valor = float(input('Salario: '))

print(f'> Fixos (água, luz, internet, feira)..................R$ {valor * 0.8:.2f}')
print(f'> Reserva de Emergência...............................R$ {valor * 0.075:.2f}')
print(f'> Lazer, Viagens......................................R$ {valor * 0.05:.2f}')
print(f'> Objet. Longo Prazo(aposentadoria, filhos, viagem)...R$ {valor * 0.075:.2f}')