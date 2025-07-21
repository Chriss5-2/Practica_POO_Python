# Creando juego de seleccionar número al azar pero con clases
import random

class SelectNumber:
    # Definiendo atributo de clase que servirá para contar el número de turnos con el que se resuelve el juego
    turnos = 0
    def __init__(self, min=1, max=2):
        self.min = min
        self.max = max
        # self.number = random.randint(self.min, self.max)
        self.number = 0

    def generate_random(self, min, max):
        """Genera un número aleatorio entre min y max."""
        self.number = random.randint(self.min, self.max)
        # print(f"{self.number}")
        return self.number

    def verify_selection(self, selection):
        """Verifica si el número seleccionado es correcto."""
        """En caso sea incorrecto, nos dirá si el número seleccionado es mayor o menos al número a adivinar."""
        if selection < self.number:
            return "El número seleccionado es menor al número a adivinar."
            self.turnos += 1
            return False
        elif selection > self.number:
            return "El número seleccionado es mayor al número a adivinar."
            self.turnos += 1
            return False
        else:
            print("¡Felicidades! Has adivinado el número.")
            print(f"El número de turnos que has utilizado es: {self.turnos + 1}")
            return True
        pass

    def requeriments(self, min, max):
        if self.min >= self.max:
            print("El valor mínimo debe ser menor que el valor máximo.")
            return False
        elif min < 0:
            print("El valor mínimo no puede ser negativo.")
            return False
        elif max < 0:
            print("El valor máximo debe ser mayor que cero.")
            return False
        else:
            return True

def main():
    """Función principal para ejecutar el juego."""
    print("Bienvenido al juego de adivinar el número.")
    min_value = int(input("Ingrese el valor mínimo: "))
    max_value = int(input("Ingrese el valor máximo: "))
    
    # Crea la instancia del juego con un número aleatorio entre min y max
    game = SelectNumber(min_value, max_value)

    # Verificamos que los valores ingresados sean válidos y en caso contrario
    # solicitamos al usuario ingresar nuevamente los valores y de acuerdo a esto
    # generamos un nuevo número aleatorio con el método generate_random
    while not game.requeriments(min_value, max_value):
        print("El valor mínimo debe ser menor que el valor máximo. Intente de nuevo.")
        min_value = game.min = int(input("Ingrese el valor mínimo: "))
        max_value = game.max = int(input("Ingrese el valor máximo: "))
    
    game.generate_random(min_value, max_value)
    
    while True:
        try:
            user_input = int(input(f"Ingrese un número entre {min_value} y {max_value}: "))
            if user_input < min_value or user_input > max_value:
                print(f"Por favor, ingrese un número dentro del rango {min_value} - {max_value}.")
                continue
            
            result = game.verify_selection(user_input)
            if result is True:
                break
            else:
                print(result)
                game.turnos += 1
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

if __name__ == "__main__":
    main()