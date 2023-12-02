def pixelab(a,b):
    pixel_por_cm = 118.12
    largura_em_px = a * pixel_por_cm
    altura_em_px = b * pixel_por_cm
    
    return f'\n> Largura.....: {largura_em_px:.2f} px\n> Altura......: {altura_em_px:.2f} px'


largura_em_cm = float(input('Largura [cm]: '))
altura_em_cm = float(input('Altura  [cm]: '))
pixels = pixelab(largura_em_cm,altura_em_cm)


print(pixels)