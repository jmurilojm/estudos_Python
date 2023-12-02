def morse(texto):
    letras = texto.upper()
    for letra in letras:
        if letra == 'A':
            print('''.|''',end = '')
        if letra == 'B':
            print('''|...''',end = '')
        if letra == 'C':
            print('''|.|.''',end = '')
        if letra == 'D':
            print('''''',end = '')
        if letra == 'E':
            print('''.''',end = '')
        if letra == 'F':
            print('''..|.''',end = '')
        if letra == 'G':
            print('''||.''',end = '')
        if letra == 'H':
            print('''....''',end = '')
        if letra == 'I':
            print('''..''',end = '')
        if letra == 'J':
            print('''.|||''',end = '')
        if letra == 'K':
            print('''|.|''',end = '')
        if letra == 'L':
            print('''.|..''',end = '')
        if letra == 'M':
            print('''||''',end = '')
        if letra == 'N':
            print('''|.''',end = '')
        if letra == 'O':
            print('''|||''',end = '')
        if letra == 'P':
            print('''.||.''',end = '')
        if letra == 'Q':
            print('''||.|''',end = '')
        if letra == 'R':
            print('''.|.''',end = '')
        if letra == 'S':
            print('''...''',end = '')
        if letra == 'T':
            print('''|''',end = '')
        if letra == 'U':
            print('''..|''',end = '')
        if letra == 'V':
            print('''...|''',end = '')
        if letra == 'W':
            print('''.||''',end = '')
        if letra == 'X':
            print('''|..|''',end = '')
        if letra == 'Y':
            print('''|.||''',end = '')
        if letra == 'Z':
            print('''||..''',end = '')
        if letra == ' ':
            print('''  ''',end = '')
            
        if letra == '1':
            print('''.||||''',end = '')
        if letra == '2':
            print('''..|||''',end = '')
        if letra == '3':
            print('''...||''',end = '')
        if letra == '4':
            print('''....|''',end = '')
        if letra == '5':
            print('''.....''',end = '')
        if letra == '6':
            print('''|....''',end = '')
        if letra == '7':
            print('''||...''',end = '')
        if letra == '8':
            print('''|||..''',end = '')
        if letra == '9':
            print('''||||.''',end = '')
        if letra == '0':
            print('''|||||''',end = '')
            pass


morse('Programando em Python')


