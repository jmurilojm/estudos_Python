def criptografar(texto):
    letras = texto.upper()
    
    cod = []
    
    for letra in letras:
        if letra == 'O' or letra == 'Ó' or letra == 'Ô' or letra == 'Õ':
            cod.append(letra.replace(letra,'0'))
            
        elif letra == 'I' or letra == 'Í':
            cod.append(letra.replace(letra,'1'))
            
        elif letra == 'Z':
            cod.append(letra.replace(letra,'2'))
            
        elif letra == 'E' or letra == 'É' or letra == 'Ê':
            cod.append(letra.replace(letra,'3'))
        
        elif letra == 'A' or letra == 'Á' or letra == 'Â' or letra == 'Ã':
            cod.append(letra.replace(letra,'4'))
        
        elif letra == 'S':
            cod.append(letra.replace(letra,'5'))
        
        elif letra == 'L':
            cod.append(letra.replace(letra,'7'))
            
        elif letra == 'G':
            cod.append(letra.replace(letra,'8'))
        
        else:
            cod.append(letra)
            
            
    for letra in cod:
        print(letra,end='')
    print()
    pass
    
    
criptografar('Prógramando em Python')

print('\n')

criptografar('Como substituir trechos de uma string utilizando expressões regulares?\nO método replace() só pode ser utilizado com um parâmetro de seleção. Isso significa que se quisermos, por exemplo, localizar em uma string a ocorrência do caractere dois pontos e também da vírgula, não será possível com esse recurso. Entretanto, podemos utilizar expressões regulares para nos ajudar nessa tarefa.\n\nVale ressaltar que as expressões regulares correspondem a um recurso muito utilizado em diversas linguagens de programação. Não entraremos em detalhes sobre sua elaboração, pois temos este guia inicial com dicas valiosas sobre o assunto, que você pode conferir mais tarde.\n\nPara utilizar expressões regulares — Python regex replace — para substituir partes de uma string, precisamos utilizar o módulo re, que é uma abreviatura de regular expression. Na prática, esse módulo contém uma série de métodos que possibilitam a utilização de expressões regulares com diferentes tipos de dados, entre eles, a string.')