#ejercicio 3 parcial 1 
class Celular  :
    def __init__(self, marca,color,forma):
        self.marca = marca
        self.color = color 
        self.forma = forma
micelular = Celular('xiaomi','negro','rectangular')

print(type(micelular))

print(micelular.marca)