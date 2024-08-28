#ejercicio 2 parcial 1 
class Mascota:
    def __init__(self,nombre,raza,color):
        self.nombre = nombre
        self.raza = raza
        self.color = color     
gato = Mascota ('catalina','angora','negro')
perro = Mascota ('mailo','criollo','amarillo y blanco')

print(type(gato))
print(type(perro ))

print(perro.nombre)
print(gato.color)