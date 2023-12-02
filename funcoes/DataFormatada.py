def diaHora():
    from datetime import datetime

    hora = datetime.now()
    data_formatada = hora.strftime('%d/%m/%y %H:%M')
    
    return data_formatada
    
    
x = diaHora()

print(x)