def switch(a):
    msg = "O valor digitado foi: "
    msg_error = "Valor inválido"
    return {
        0: f"{msg} {a}", 
        1: f"{msg} {a}",
        2: f"{msg} {a}",
        3: f"{msg} {a}",
        4: f"{msg} {a}",
        5: f"{msg} {a}",
        }.get(a, f"{msg_error}")
        
def swit(a):
    msg = "O valor digitado foi: "
    msg_error = "Valor inválido"
    if a == 0:
        return f"{msg} {a}"
    elif a == 1:
        return f"{msg} {a}"
    else:
        return f"{msg_error}"
    
    
n = int(input('Digite 0 ou 1: '))
s = switch(n)
t = swit(n)

print(f"{s}\n{t}")