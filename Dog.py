class Dog:
    species = "Canis familiaris" 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Métodos o métodos de instancia son funciones definidas dentro de una clase
    # y pueden ser llamadas solo por una instancia de esa clase
    
    # Método de instancia que devuelve el nombre y la edad del perro
    def descrition(self):
        return f"{self.name} is {self.age} years old"

    # Método que devuelve el sonido que hace el perro
    def speak(self, sound): # Este método recibe un parámetro 'sound'
        return f"{self.name} says {sound}"


class Dog_modify:
    species = "Canis familiaris" 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Método de instancia que devuelve el nombre y la edad del perro
    def descrition(self):
        return f"{self.name} is {self.age} years old"

    # Método que devuelve el sonido que hace el perro
    def speak(self, sound): # Este método recibe un parámetro 'sound'
        return f"{self.name} says {sound}"

    def __str__(self):
        return f"{self.name} is ({self.age} years old)"


class Dog_breed():
    species = "Canis familiaris" 
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Método de instancia que devuelve el nombre, la edad y la raza del perro
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Método que devuelve el sonido que hace el perro
    def speak(self, sound): # Este método recibe un parámetro 'sound'
        return f"{self.name} says {sound}"

class Dog_2:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        #return f"{self.name} barks: {sound}"
        return f"{self.name} says {sound}"