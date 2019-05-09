from Puntos import *
from Figuras import *

class Triangulo(Figuras):

    def calculararea(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.area = (p3.distancia(self.p1) * p3.distancia(self.p2))/2

    def calcularperimetro(self):
        p3 = Punto()
        p3.x = self.p1.x
        p3.y = self.p2.y
        self.perimetro = p3.distancia(self.p1) + p3.distancia(self.p2) + self.p1.distancia(self.p2)
   



