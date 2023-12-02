from tkinter import *

calc = Tk()

tela = Label(calc, text='Calculo')
tela['width'] = 40
tela['height'] = 13
tela['bg'] = 'white'
tela.place(x=15,y=20)

# Linha 1
b1 = Button(calc)
b1['bg'] = 'yellow'
b1['width'] = 5
b1['height'] = 4
b1['text'] = 'Limpar'
b1.place(x=20,y=2000)

b2 = Button(calc)
b2['bg'] = 'yellow'
b2['width'] = 5
b2['height'] = 4
b2['text'] = '0'
b2.place(x=290,y=2000)

b3 = Button(calc)
b3['bg'] = 'yellow'
b3['width'] = 5
b3['height'] = 4
b3['text'] = '.'
b3.place(x=555,y=2000)

b4 = Button(calc)
b4['bg'] = 'yellow'
b4['width'] = 5
b4['height'] = 4
b4['text'] = '='
b4.place(x=820,y=2000)

# Linha 2
b5 = Button(calc)
b5['bg'] = 'yellow'
b5['width'] = 5
b5['height'] = 4
b5['text'] = '1'
b5.place(x=20,y=1700)

b6 = Button(calc)
b6['bg'] = 'yellow'
b6['width'] = 5
b6['height'] = 4
b6['text'] = '2'
b6.place(x=290,y=1700)

b7 = Button(calc)
b7['bg'] = 'yellow'
b7['width'] = 5
b7['height'] = 4
b7['text'] = '3'
b7.place(x=555,y=1700)

b8 = Button(calc)
b8['bg'] = 'yellow'
b8['width'] = 5
b8['height'] = 4
b8['text'] = '+'
b8.place(x=820,y=1700)

# Linha 3
b9 = Button(calc)
b9['bg'] = 'yellow'
b9['width'] = 5
b9['height'] = 4
b9['text'] = '4'
b9.place(x=20,y=1400)

b10 = Button(calc)
b10['bg'] = 'yellow'
b10['width'] = 5
b10['height'] = 4
b10['text'] = '5'
b10.place(x=290,y=1400)

b11 = Button(calc)
b11['bg'] = 'yellow'
b11['width'] = 5
b11['height'] = 4
b11['text'] = '6'
b11.place(x=555,y=1400)

b12 = Button(calc)
b12['bg'] = 'yellow'
b12['width'] = 5
b12['height'] = 4
b12['text'] = '-'
b12.place(x=820,y=1400)

# Linha 4
b13 = Button(calc)
b13['bg'] = 'yellow'
b13['width'] = 5
b13['height'] = 4
b13['text'] = '7'
b13.place(x=20,y=1100)

b14 = Button(calc)
b14['bg'] = 'yellow'
b14['width'] = 5
b14['height'] = 4
b14['text'] = '8'
b14.place(x=290,y=1100)

b15 = Button(calc)
b15['bg'] = 'yellow'
b15['width'] = 5
b15['height'] = 4
b15['text'] = '9'
b15.place(x=555,y=1100)

b16 = Button(calc)
b16['bg'] = 'yellow'
b16['width'] = 5
b16['height'] = 4
b16['text'] = 'x'
b16.place(x=820,y=1100)

# Linha 5
b17 = Button(calc)
b17['bg'] = 'yellow'
b17['width'] = 5
b17['height'] = 4
b17['text'] = 'x²'
b17.place(x=20,y=800)

b18 = Button(calc)
b18['bg'] = 'yellow'
b18['width'] = 5
b18['height'] = 4
b18['text'] = '√'
b18.place(x=290,y=800)

b19 = Button(calc)
b19['bg'] = 'yellow'
b19['width'] = 5
b19['height'] = 4
b19['text'] = '%'
b19.place(x=555,y=800)

b20 = Button(calc)
b20['bg'] = 'yellow'
b20['width'] = 5
b20['height'] = 4
b20['text'] = '÷'
b20.place(x=820,y=800)


calc.title('Calculadora')
calc.mainloop()
