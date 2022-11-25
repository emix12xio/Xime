from tkinter import*

root = Tk()

root.geometry('400x400')

root.title('menu ejemplo')

menubar = Menu(root)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='archivo', menu=file)
file.add_command(label='nuevo archivo')
file.add_command(label='abrir')
file.add_command(label='guardar')

edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='modificar', menu=edit)
edit.add_command(label='cortar')
edit.add_command(label='copiar')
edit.add_command(label='pegar')
edit.add_command(label='seleccionar todo')

help_=Menu(menubar, tearoff=0)
menubar.add_cascade(label='ayuda', menu=help_)
help_.add_command(label='preguntas frecuentes')
help_.add_command(label='acerda de...')

root.config(menu=menubar)

root.mainloop()
