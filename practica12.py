class geo:
    def __init__(self):
        self.a= int(input('dame el numero base:'))
        self.b= int(input('dame el numero de altura:'))


    def imprimir(self):
        print(f'base:',self.a)
        print(f'altura:',self.b)
        print('el area es:',(self.a * self.b)/2)


x=geo()
x.imprimir()
