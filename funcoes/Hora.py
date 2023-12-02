def hora():
    from datetime import datetime

    data = datetime.now()
    hora = data.strftime('%H:%M')
    
    return hora
    
    
x = hora()

print(x)