class menu:
    def __init__(self):
        self.nombres=input('registra tu nombres')
        self.apellidos=input('registra tu apellidos')
        self.edad=int(input('registra tu edad'))
        self.grado=input('registra tu grado')
        self.seccion=input('registra tu seccion')
        self.ID=int(input('registra tu ID'))
        self.direccion=input('registra tu direccion')
        self.telefono=input('registra tu telefono')
class personal(menu):
    def nombres(self):
        print(f'nombres:', self.nombres)
    def apellidos(self):
        print(f'apellidos:', self.apellido)
    def edad(self):
        print(f'edad:', self.edad)
class educacion(menu):        
    def grado(self):
        print(f'grado:', self.grado)
    def seccion(self):
        print(f'seccion:', self.seccion)
    def ID(self):
        print(f'ID:', self.ID)
class contacto(menu):        
    def direccion(self):
        print(f'direccion:', self.direccion)
    def telefono(self):
        print(f'telefono:', self.telefono)
x=menu()        
y =0
while y < 5:
    print('bienvenido al menu')
    print('-----------')
    print('1. datos personales')
    print('2. datos escolares')
    print('3. datos de contacto')
    print('4. salir')
    print('---------------')
    
    op= input('que desea registrar?')

    x = menu()
    h = personal()
    k = educacion()
    j = contacto()


    if op ==1:
        h.personal
    if op ==2:
        k.educacion
    if op ==3:
        j.contacto
    if op ==4:
        print('estas saliendo del sistema, vuelve pronto')
        y=10
x = menu()
h = personal()
k = educacion()
j = contacto()



    
