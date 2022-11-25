import tkinter as tk
def accion1():
    texto.configure(text='Has elegido la opción 1 del menú principal')
def accion2():
    texto.configure(text='Has elegido la opción 2 del menú principal')
def acciona():
    texto.configure(text='Has elegido la opción a del submenú')
def accionb():
    texto.configure(text='Has elegido la opción b del submenú')

ventana = tk.Tk()
ventana.title('Ventana principal')
ventana.geometry('800x600')
barra_menus = tk.Menu(ventana)
ventana.config(menu=barra_menus)
menu = tk.Menu(barra_menus, tearoff=False)
menu.add_command(label='Opción 1', command=accion1)
menu.add_command(label='Opción 2', command=accion2)
submenu = tk.Menu(menu, tearoff=False)
submenu.add_command(label='Opción A', command=acciona)
submenu.add_command(label='Opción B', command=accionb)
menu.add_cascade(label='Submenú', menu=submenu)
menu.add_separator()
menu.add_command(label='Salir', command=ventana.destroy)
barra_menus.add_cascade(label="Menú", menu=menu)
texto = tk.Label(ventana, text='hola,como estas')
texto.place(x=200, y=200)
if __name__ == '__main__':
    ventana.mainloop()  
