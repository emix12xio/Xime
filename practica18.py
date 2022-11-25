import tkinter as tk
def accion1():
    texto.configure(text='Has elegido la opci�n 1 del men� principal')
def accion2():
    texto.configure(text='Has elegido la opci�n 2 del men� principal')
def acciona():
    texto.configure(text='Has elegido la opci�n a del submen�')
def accionb():
    texto.configure(text='Has elegido la opci�n b del submen�')

ventana = tk.Tk()
ventana.title('Ventana principal')
ventana.geometry('800x600')
barra_menus = tk.Menu(ventana)
ventana.config(menu=barra_menus)
menu = tk.Menu(barra_menus, tearoff=False)
menu.add_command(label='Opci�n 1', command=accion1)
menu.add_command(label='Opci�n 2', command=accion2)
submenu = tk.Menu(menu, tearoff=False)
submenu.add_command(label='Opci�n A', command=acciona)
submenu.add_command(label='Opci�n B', command=accionb)
menu.add_cascade(label='Submen�', menu=submenu)
menu.add_separator()
menu.add_command(label='Salir', command=ventana.destroy)
barra_menus.add_cascade(label="Men�", menu=menu)
texto = tk.Label(ventana, text='hola,como estas')
texto.place(x=200, y=200)
if __name__ == '__main__':
    ventana.mainloop()  
