def dia():
    import time
    
    dia = time.ctime()
    
    if 'Sun' in dia:
        return 'Domingo'
    elif 'Mon' in dia:
        return 'Segunda-feira'
    elif 'Tue' in dia:
        return 'Terça-feira'
    elif 'Wed' in dia:
        return 'Quarta-feira'
    elif 'Thu' in dia:
        return 'Quinta-feira'
    elif 'Fri' in dia:
        return 'Sexta-feira'
    elif 'Sat' in dia:
        return 'Sábado'

        
x= dia()

print(x)