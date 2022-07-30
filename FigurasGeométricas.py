class Figura:
    pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado 

    def perimetro(self):
        return self.lado * 4

class Rectangulo(Figura):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1 
        self.lado2 = lado2 

    def perimetro(self):
        return 2*self.lado1 + 2*self.lado2

# TODO: Pensar en otra posible herencia (taxonomía)
# la clase Triangulo

class Triangulo(Figura):
    def __init__(self, lado1,lado2,lado3):
        self.lado1 = lado1 
        self.lado2 = lado2 
        self.lado3 = lado3 
         
    
    def perimetro(self):
        if (self.lado1+self.lado2>self.lado3 and self.lado2+self.lado3>self.lado1 and self.lado1+self.lado3>self.lado2):
            print("La figura es un triángulo")
            return self.lado1 + self.lado2+ self.lado3
        else:
            print("No es un triángulo")
    




# Pruebas
c1 = Cuadrado(6)
c2 = Cuadrado(4)
print(c1.perimetro())
print(c2.perimetro())

r1 = Rectangulo(3,4)
r2 = Rectangulo(4,10)
print(r1.perimetro())
print(r2.perimetro())


t1=Triangulo(3,4,5)
t2=Triangulo(1,3,4)
print(t1.perimetro())
print(t2.perimetro())