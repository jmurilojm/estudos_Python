def area_cubica(largura,profunfidade,altura):
  '''
  E necessario inserir tres dados na seguinte ordem:
  - largura
  - profundidade
  - altura
  '''
  return largura * profunfidade * altura


larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
alt = float(input('Altura: '))

resultado = area_cubica(larg,comp,alt)
print(resultado)