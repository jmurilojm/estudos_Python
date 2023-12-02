import tkinter

janela = tkinter.Tk()

janela.title('Janela JM')
janela.geometry('300x200')

frame1 = tkinter.Frame(janela,bg='yellow')
frame1.pack(fill='both', expand=True, side='top')

frame2 = tkinter.Frame(janela,bg='blue')
frame2.pack(fill='both', expand=True, side='bottom')

janela.mainloop()