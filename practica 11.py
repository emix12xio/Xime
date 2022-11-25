class poligono:
    def __init__(self, b, h):
        self.b = b
        self.h = h

class rectangulo(poligono):

    def area(self):
        return self.b * self.h


class triangulo(poligono):

    def area(self):
        return (self.b * self.h)/ 2

rectangulo1 = rectangulo(20, 10)
triangulo1 = triangulo(20, 12)

print('Área del rectángulo: ', rectangulo1.area())
print('Área del triángulo: ', triangulo1.area())
