import sys

main=sys.argv[1] if len(sys.argv) > 1 else print("Agregue un argumento: 'Persona', 'Dog', 'Dog_1', 'Dog_modify', 'Ejercicio_1', 'Parent_1', 'Dog_breed', 'Dog_child_1', 'Dog_child_2', 'Ejercicio_2' \n Ejemplo de ejecución: python POO.py Persona")

class Persona:
    # Declaración de atributos de la clase
    def __init__ (self, nombre, edad, dirección):
        self.nombre = nombre
        self.edad = edad
        self.dirección = dirección

    def name(self):
        return self.nombre

    def age(self):
        return self.edad
    
    def address(self):
        return self.dirección

def main_1():
    persona=Persona("Christian", 22, "Callao")
    print(persona.name())
    print(persona.age())
    print(persona.address())
    print(persona.__dict__)


class Lista:
    def __init__(self, nombre, edad, puesto, año_inicio):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        self.año_inicio = año_inicio

    # Esta clase es para crear una lista de empleados pero sin usar listas sino designarlos como atributos en una clase

    def add_employ(self, nombre, edad, puesto, año_inicio):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        self.año_inicio = año_inicio

    def show_employ(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}, Año de Inicio: {self.año_inicio}'

    def show_all_employees(self):
        return f'Empleado: {self.nombre}, Edad: {self.edad}, Puesto: {self.puesto}, Año de Inicio: {self.año_inicio}'

    # Aún falta implementar funcionalidad para tener múltiples empleados


# Ejemplo de https://realpython.com/python3-object-oriented-programming/
class Example:
    # CLase: Modelo para defiinir algo - No contiene datos
    # Instancia: Es el objeto creado a partir de una clase - Contiene datos - Ya no es un modelo
    # La clase es como un formulario vacío donde el usuario ingresa información única
    pass
    # El 'pass' indica que no hay nada que hacer en este momento
    # https://realpython.com/python-pass/
    # La sentencia 'pass' indica al sistema a no hacer nada en ese momentos


# Ejemplo de clase sin métodos y solo con atributos
class Dog:
    # Definiendo atributo general
    species = "Canis familiaris"  # Atributo de clase, compartido por todas las instancias
    # Todas las instancias que se creen, tendrán ese atributo por defecto
    def __init__(self, name, age):
        # Crea un atributo llamado 'name' y le asigna el valor del parámetro 'name'
        self.name = name
        # Crea un atributo llamado 'age' y le asigna el valor del parámetro 'age'
        self.age = age

def main_2():
    dog_1=Dog("Firulais", 5)
    dog_2=Dog("Firulais", 5)
    # Comparando dos instancias con los mismos valores
    print(dog_1==dog_2) # False <Dos instancias con parámetros iguales NO son iguales>

    # Verifiando el tipo de dato de las instancias
    print(type(dog_1)) # <class '__main__.Dog'>

    # Verificando el tipo de dato de la clase Dog
    print(type(Dog("Firulais", 5))) # <class '__main__.Dog'>

    # Nos muestra la dirección de memoria donde se encuentra el objeto o la instancia
    print(Dog("Firulais", 5)) # <__main__.Dog object at 0x0000025ED3D9EAB0>
    # El valor en cada ejecución es diferente, ya que se guarda en una dirección de memoria diferente
    
    # Al crear una instancia de Dog, se necesita pasar parámetros de 'name' y 'age' porque sino nos dará error
    # El error generado es: TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'

    # Acceder a ls atributos de las instancias
    print("Accediendo a los atributos de las instancias:")
    # Recordar que 'name' y 'age' son atributos de instancia, no de clase"
    # Recordar que 'species' es un atributo de clase, no de instancia
    # Basicamente 'name' y 'age' son atributos únicos de cada instancia y 'species' es un atributo compartido por todas las instancias
    # 'species' es un atributo de clase
    # 'species' es igual para todas las instancias de la clase Dog
    # 'name' y 'age' son distintos para cada instancia de la clase Dog
        # Accediendo a atributos propios de las instancias
    # Accediendo al atributo 'name'
    print("Instancia 1:", dog_1.name)
    print("Instancia 2:", dog_2.name)

    # Accediendo al atributo 'age'
    print("Instancia 1:", dog_1.age)
    print("Instancia 2:", dog_2.age)
        # Accediendo al atributo 'species' 
    print("Instancia 1:", dog_1.species)
    print("Instancia 2:", dog_2.species)
        # Verificando si el atributo 'species' es el mismo para ambas instancias
    print("Iguales?: ", dog_1.species == dog_2.species) # True

        # Verificando si el atributo 'name' es el mismo para ambas instancias
    print("Iguales?: ", dog_1.name == dog_2.name) # True
    # Serán iguales porque ambos tienen el mismo string "Firulais"
    # Como instancias no son iguales, pero sus atributos pueden ser iguales

    # Los atributos de las instancias se pueden modificar
    dog_1.name = "Rex"
    print("Modificando el atributo 'name' de la instancia 1")
    print("Instancia 1:", dog_1.name) # Rex
    print("Instancia 2:", dog_2.name) # Firulais
    # Se pueden modificar los atributos de instancia y los atributos de clase sin problemas
    print("Modificando el atributo 'species' de la instancia 1")
    dog_1.species = "Canis lupus familiaris"
    print("Instancia 1:", dog_1.species) # Canis lupus familiaris
    print("Instancia 2:", dog_2.species) # Canis lupus familiar
    
    # Pero también se pueden modificar los atributos de clase directamente de forma global
    print("Modificando el atributo 'species' de la clase Dog")
    Dog.species = "New specie"
    print("Instancia 1:", dog_1.species) # Canis lupus familiar
    print("Instancia 2:", dog_2.species) # New specie
    # Si no se actualiza de manera particular a una instancia, al actualizar la variable global, esta se cambiará para la instancia no modificada
    # dog_1.species no se actualiza porque ya había sido modificado anteriormente

    # Los objetos personalizados son mutables, es decir, pueden ser modificados después de su creación



# Ejemplo de clase con métodos y atributos
class Dog_1:
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

def main_3():
    dog_1 = Dog_1("Firulais", 5)
    dog_2 = Dog_1("Rex", 3)

    # Llamando al método 'descrition' de la instancia 'dog_1'
    print("Descripción del perro 1: ", dog_1.descrition())  # Firulais is 5 years old
    print("Descripción del perro 2: ", dog_2.descrition())  #

    # Llamando al método 'speak' de la instancia 'dog_2'
    print("Sonido del perro 1: ", dog_1.speak("Bow Wow"))  # Firulais says Bark
    print("Sonido del perro 2: ", dog_2.speak("Woof Woof"))  # Rex says Woof Woof


# Creando la clase en un archivo separado
# POO.py
def main_4():
    from Dog import Dog as Dog_file
    from Dog import Dog_modify as Dog_modify_file
    print("Creando instancias de la clase Dog desde un archivo separado")
    # Para crear se importa desde el nombre o alias asignado al importar la clase Dog del archivo Dog.py
    # En este caso se llamó Dog_file a la importación de la clase Dog
    dog_1 = Dog_file("Firulais", 5)
    dog_2 = Dog_file("Rex", 3)

    # Llamando al método 'descrition' de la instancia 'dog_1'
    print("Descripción del perro 1: ", dog_1.descrition())  # Firulais is 5 years old
    print("Descripción del perro 2: ", dog_2.descrition())  # Rex is 3 years old

    # Llamando al método 'speak' de la instancia 'dog_2'
    print("Sonido del perro 1: ", dog_1.speak("Bow Wow"))  # Firulais says Bow Wow
    print("Sonido del perro 2: ", dog_2.speak("Woof Woof"))  # Rex says Woof Woof

    # Llamando la dirección de memoria de las instancias
    print("Dirección de memoria del perro 1: ", dog_1)  # <__main__.Dog object at 0x...>
    print("Dirección de memoria del perro 2: ", dog_2)  # <__main__.Dog object at 0x...>


    # Para modificar el valor del retorno al llamar a la instancia sin solicitar algún atributo
    # Se cre un método __str__ en la clase usada y se retorna un string personalizado
    print("Modificando el retorno de la instancia al llamarla directamente <'Creando método __str__ en la clase Dog_modify'>")
    dog_1_m= Dog_modify_file("Firulais", 5)
    dog_2_m= Dog_modify_file("Rex", 3)
    print("Descripción modificada del perro 1: ", dog_1_m)  # Firulais is (5 years old)
    print("Descripción modificada del perro 2: ", dog_2_m)  # Rex is (3 years old)
    # El método __init__ y __str__ son llamados dunder methods o métodos mágicos


# Resolviendo el ejercicio 1 de la página
# https://realpython.com/python3-object-oriented-programming/#:~:text=If%20you%20want%20to%20reinforce%20your%20understanding%20with%20a%20practical%20exercise%2C%20then%20you%20can%20click%20on%20the%20block%20below%20and%20work%20on%20solving%20the%20challenge%3A
def ejercicio_1():
    class Car:
        def __init__(self, color, mileage):
            self.color = color
            self.mileage = mileage

        def __str__(self):
            return f"The {self.color} car has {self.mileage} miles."

    car_1 = Car("blue", 20000)
    car_2 = Car("red", 30000)
    print("Imprimiendo el objeto directamente - Individualmente")
    print(car_1)  # The blue car has 20000 miles.
    print(car_2)  # The red car has 30000 miles.

    # Imprimiento el objeto dentro de una iteración
    print("Imprimiendo el objeto dentro de una iteración")
    for car in (car_1, car_2):
        print(car)

# Recordatorio
### Si no se crea el método __str__ en la clase, al imprimir el objeto directamente, se mostrará la dirección de memoria del objeto



# Práctica de herencia
class Parent:
    hair_color = "brown"
class Child(Parent):
    pass
class Child_2(Parent):
    hair_color = "purple"

class Parent_m:
    speaks = ["English"]
class Child_3(Parent_m):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")

def main_5():
    print("Práctica de herencia")
    child = Child()
    print("El color de cabello del padre es:", Parent.hair_color)  # brown
    print("El color de cabello del hijo es:", child.hair_color)  # brown
    # Los hijos heredan TODOS los atributos y métodos de la clase padre
    # Los hijos también puedes tener sus propios atributos y métodos
    # Modificando atributo heredado
    print("Modificando el atributo 'hair_color' en la clase Child_2")
    child_2 = Child_2()
    print("El color de cabello del hijo es:", child_2.hair_color)
    
    # Heredando una lista de atributos y modificandola en el hijo
    print("Heredando una lista de atributos y modificandola en el hijo")
    child_3 = Child_3()
    print("El hijo habla:", child_3.speaks)  # ['English', 'German']


# Clase perro que incluya las razas
def main_6():
    from Dog import Dog_breed as Dog_breed_file
    dog_breed = Dog_breed_file("Firulais", 5, "Labrador")
    print("Descripción del perro con raza: ", dog_breed)  # Firulais is 5 years old
    print("Raza del perro: ", dog_breed.breed)  # Labrador
    # speak es el sonido de ladrido que hace el perro
    print("Sonido del perro: ", dog_breed.speak("Woof Woof"))  # Firulais says Woof Woof
    # De manera general, el ladrido <atributo-speak> del perro debe depender de la raza del perro <atributo-breed>
    # Para realizar ello, se podrían generar hijos a partir de la clase Dog_breed de acuerdo a la raza del perro y con esto se modificará el sonido del perro


# Para aplicar lo dicho antes, se crearán clases hijo de acuerdo a tres razas de perros
# Para esta parte se agregará la clase Dog_2 para aplicarlo con las razas de perro
def main_7():
    from Dog import Dog_2 as Dog_example
    # Creando clase de un perro de la raza JackRusselTerrier
    class JackRusselTerrier(Dog_example):
        pass

    # Perro de la raza Dachshund
    class Dachshund(Dog_example):
        pass

    # Perro de la raza Bulldog
    class Bulldog(Dog_example):
        pass

    # Creando instancias de las razas con las clases hijas
    dog_1 = JackRusselTerrier("Firulais", 5)
    dog_2 = Dachshund("Rex", 3)
    dog_3 = Bulldog("Bobby", 4)

    # Verificando la especia (son heredadas de la clase Dog así que la especie es la misma)
    print("Especies de todos los perros:")
    print("Perro 1:", dog_1.species)  # Canis familiaris
    print("Perro 2:", dog_2.species)  # Canis familiaris
    print("Perro 3:", dog_3.species)  # Canis familiaris

    # Verificando método __str__ para cada raza - También se hereda de Dog
    print("Método __str__ de cada raza:")
    print("Perro 1:", dog_1)  # <__main__.JackRusselTerrier object at 0x...>
    print("Perro 2:", dog_2)  # <__main__.Dachshund object at 0x...>
    print("Perro 3:", dog_3)  # <__main__.Bul
    
    # Agregando ladrido a cada instancia de clase hija
    print("Ladrido de cada perro:")
    print("Perro 1:", dog_1.speak("Bark Bark"))
    print("Perro 2:", dog_2.speak("Woof Woof"))
    print("Perro 3:", dog_3.speak("Grr Grr"))

    # Vericiando el tipo de dato de cada instancia
    print("Tipo de dato de cada perro:")
    print("Perro 1:", type(dog_1))  # <class '__main__.JackRusselTerrier'>
    print("Perro 2:", type(dog_2))  # <class '__main__.Dachshund'>
    print("Perro 3:", type(dog_3))  # <class '__main__.Bulldog'>
    # Notamos que nos muestra el nombre de la clase hija de cual hereda la instancia

    # Verificar si un objeto es una instancia de una clase
    print("Verificando si cada perro es una instancia de Dog:")
    print("Perro 1 es instancia de Dog:", isinstance(dog_1, Dog_example))  # True
    print("Perro 2 es instancia de Dog:", isinstance(dog_2, Dog_example))  # True
    print("Perro 3 es instancia de Dog:", isinstance(dog_3, Dog_example))  # True
    # La respuesta será <True> porque todas las clases heredan de la clase Dog_2 la cual es la clase padre
    
    # También podemos verificar estas instancias con las clases hijas
    print("Verificando si cada perro es una instancia de su clase hija:")
    print("Perro 1 es instancia de JackRusselTerrier:", isinstance(dog_1, JackRusselTerrier))  # True
    print("Perro 2 es instancia de Dachshund:", isinstance(dog_2, Dachshund))  # True
    print("Perro 3 es instancia de Bulldog:", isinstance(dog_3, Bulldog))  # True
    # El método isistance() verifica si el primer parámetro es una instancia del segundo parámetro y de acuerdo a esto devuelve <True> or <False>
    # Sirve tanto para verificar de una instancia a la clase padre o a la clase hija de la cuál hereda

    # Para verificar cuando es False, verificamos si son una instancia de una clase hija a la cuál no pertenecen
    # Tomar en cuenta:
    # dog_1 es una instancia de JackRusselTerrier
    # dog_2 es una instancia de Dachshund
    # dog_3 es una instancia de Bulldog
    print("Verificando si cada perro es una instancia de una clase hija diferente:")
    print("Perro 1 es instancia de Dachshund:", isinstance(dog_1, Dachshund))  # False
    print("Perro 2 es instancia de Bulldog:", isinstance(dog_2, Bulldog))  # False
    print("Perro 3 es instancia de JackRusselTerrier:", isinstance(dog_3, JackRusselTerrier))  # False
    # "Todaos los objetos creados de una clase hija son instancias de la clase padre aunque no pueden ser instancias de otras clases hijas"
    # Link: https://realpython.com/python3-object-oriented-programming/#:~:text=More%20generally%2C%20all%20objects%20created%20from%20a%20child%20class%20are%20instances%20of%20the%20parent%20class%2C%20although%20they%20may%20not%20be%20instances%20of%20other%20child%20classes.



# Para el siguiente ejemplo, lo que se hará será crear nuevamente clases hijas de cada raza
# pero ahora a las clases hijas se les agregará un método speak el cuál tendrá como parámetro <sound>
# el cuál tendrá un valor por defecto "Arf" y nos retornará "<nombre> says <soung>"
def main_8():
    from Dog import Dog_2 as Dog_example
    # Creando clase de un perro de la raza JackRusselTerrier
    # con método speak propio
    class JackRusselTerrier(Dog_example):
        def speak(self, sound="Arf"):
            return f"{self.name} says {sound}"

    # Creando instancia de la clase hija JackRusselTerrier
    dog_1  = JackRusselTerrier("Firulais", 5)
    # Verificando el método speak de la instancia
    print("Método speak con parámetro por defecto")
    print("Ladrido del perro 1:", dog_1.speak())  # Firulais says Arf
    
    # Como se puede ver en el método speak, tiene un parámetro <sound> con valor por defecto
    # pero también podemos agregarle un valor diferente en ese parámetro
    print("Método speak con parámetro modificado")
    print("Ladrido del perro 1:", dog_1.speak("Grr"))  # Firulais says Woof Woof
    
    # Debemos tener en cuenta que si a la clase padre que es Dog_2, se le modifica el método speak
    # esta modificación se verá reflejada en las clases hijas tambien, por ejemplo
    # si a la clase Dog_2 que se tiene en Dog.py se le modifica el retorno del método speak por
    # return f"{self.name} barks: {sound}"
    # entonces al llamar al método speak de la instancia dog_2, nos retornará "Rex barks: <sound>"
    # Para probar esto, puede comentar la línea 64 de Dog.py y descomentar la línea 63 de Dog.py
    # y luego ejecutar el archivo POO.py con el argumento 'Dog_child_2'
    # > python POO.py Dog_child_2
    # y verá que ahora la línea 391 imprimirá en pantalla "Rex barks: Woof Woof"
    class Bulldog(Dog_example):
        pass
    dog_2 = Bulldog("Rex", 3)
    print("Creando instancia de la clase Bulldog para probar modificación del método speak en la clase padre Dog_2")
    print("Ladrido del perro 2:", dog_2.speak("Woof Woof"))  # Rex says Woof Woof
    # La línea 371 seguirá imprimiendo "Firulais says Arf" porque la clase hija JackRusselTerrier
    # tiene su propio método speak así que modificar este método de la clase padre Dog_2 no le afecta a su método propio

    # Para tener una clase hija con un método speak propio pero que se vea afectada por los cambios del mismo método en la clase padre de la que hereda
    # podemos usar el método super() para llamar al método de la clase padre en la clase hija y así modificarlo según se necesite
    class Chihuahua(Dog_example):
        def speak(self, sound="Arf"):
            return super().speak(sound)

    # Con la clase hija Chihuahua, se llama al método speak de la clase padre Dog_2
    # Y se le llama con el parámetro <sound> que se le pase al método
    dog_3 = Chihuahua("Chiquitín", 2)
    print("Creando instancia de clase hija Chihuahua con método super() para llamar al método speak")
    print("Método speak original")
    print("Ladrido del perro 3:", dog_3.speak())  # Chiquitín says Arf
    print("Método speak modificado")
    print("Ladrido del perro 3:", dog_3.speak("Guau Guau"))  # Chiquitín says Guau Guau
    # Aquí podemos notar que la clase hija Chihuahua tiene su propio método speak
    # pero si se modifica el retorno del método speak de la clase padre Dog_2
    # esta modificación se verá reflejada en la clase hija Chihuahua a pesar
    # de que tenga su propio método speak, ya que se está llamando al método de la clase padre con super()



# Resolviendo ejercicio 2 de la página
# https://realpython.com/python3-object-oriented-programming/#:~:text=the%20block%20below-,and%20work%20on%20solving%20the%20challenge%3A,-Exercise%3A%20Class%20Inheritance
def ejercicio_2():
    class Dog:
        species = "Canis familiaris"

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"{self.name} is {self.age} years old"

        def speak(self, sound):
            return f"{self.name} says {sound}"
    # Creando clase hija: GoldenRetriever que tiene el método speak con valor por defecto "Bark"
    # y usa el método super() para llamar al método speak de la clase padre Dog
    class GoldenRetriever(Dog):
        def speak(self, sound="Bark"):
            return super().speak(sound)
    dog_1 = GoldenRetriever("Buddy", 3)
    print("Llamando datos de la instancia de la clase GoldenRetriever")
    print(dog_1.__dict__)
    print("Descripción del perro:", dog_1)  # Buddy is 3 years old
    print("Nombre del perro:", dog_1.name)  # Buddy
    print("Edad del perro:", dog_1.age)  # 3
    print("Especie del perro:", dog_1.species)  # Canis familiaris
    print("Imprimiendo sonido por defecto del perro")
    print("Sonido del perro:", dog_1.speak())  # Buddy says Bark
    print("Imprimiendo sonido modificado del perro")
    print("Sonido del perro:", dog_1.speak("Woof Woof"))  # Buddy says Woof Woof








if __name__ == "__main__":
    if main == "Persona":
        main_1()
    elif main == "Dog":
        main_2()
    elif main == "Dog_1":
        main_3()
    elif main == "Dog_modify":
        main_4()
    elif main == "Ejercicio_1":
        ejercicio_1()
    elif main == "Parent_1":
        main_5()
    elif main == "Dog_breed":
        main_6()
    elif main == "Dog_child_1":
        main_7()
    elif main == "Dog_child_2":
        main_8()
    elif main == "Ejercicio_2":
        ejercicio_2()
    else:
        pass
    