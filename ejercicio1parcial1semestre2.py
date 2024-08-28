##ejercicio 1 parcial 1
class Humano:
    def __init__(self, edad, estatura, peso):
        self.edad = edad
        self.estatura = estatura 
        self.peso = peso

yeison = Humano(21,1.74, 70)
andres = Humano(15,1.63,64)
print(type(yeison))
print(type(andres ))
print(yeison.edad)

