class geo:
    def __init__(self):
        self.a= input('dame tu nombre:')
        self.b= input('dame tu apellido:')
        self.c= input('dame tu grado:')
        self.d= int(input('dame tu edad:'))
        self.e= float(input('dame tu altura:'))                 

    def datos(self):
        print(f'nombre:',self.a)
        print(f'apellido:',self.b)
        print(f'grado:',self.c)
        print(f'edad:',self.d)
        print(f'altura:',self.e)
    #def imprimir(self):   


x=geo()
print('los datos regristados son')
x.datos()
#x.imprimir()
