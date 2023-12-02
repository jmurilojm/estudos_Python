def auto(texto):
    import time
    
    for letra in texto:
        print(letra,end='',flush=True)
        time.sleep(0.2)
        
        
        
auto('Programando em Python')