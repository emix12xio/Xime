class musica:

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def trap(self):
        return self.nota

    def rock(self):
        return self.nota

    def clasica(self):
        if self.nota > 6:
            print(f'aprobo el estudiante', self.nombre, 'con la nota:', self.nota)
        else:
            print(f'desaprobo el estudiante', self.nombre, 'con la nota:', self.nota)
   

            
x = musica('emma',7)
x.clasica()


   
   
        










              
              
