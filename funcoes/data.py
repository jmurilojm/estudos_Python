def data():
    from datetime import datetime

    hora = datetime.now()
    data = hora.strftime('%d/%m/%y')
    
    return data
    
    
x = data()

print(x)