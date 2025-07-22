# Para este juego, lo que haremos será tomar la mecánica del juego '21' donde tenemos que elejir números al azar
# y que los números sumados no superen el número 21
# En el juego original, esto se juega con cartas, pero ahora simularemos el lanzamiento de un dado
# Por lo que al pedir un número, se asignará un número al azar entre 1 y 6
# El jugador decidirá si seguir lanzando el dado o no
# Cuando el jugador decide no seguir, se termina el juego y se verifica la suma total
# Si la suma total de puntos obtenidos supera a 21, se pierde
# pero en caso sume 21, se gana
# pero si la suma es menor a 21, se verifica el número siguiente
# si este número al sumarlo con el total es mayor a 21, se gana
# pero si este numero al sumarlo con el total es menor o igual a 21, se pierde

from ast import Pass
import random
import sys
import os

class Dado:
    def __init__(self):
        self.valor = 0

    def lanzar(self):
        self.valor = random.randint(1, 6)
        return self.valor

# Se crea la clase Juego21 que contendrá toda la lógica del juego
# Los atributos de la clase serán: 
# 'total' <conteo de puntos obtenidos>
# 'dado' <instancia de la clase Dado>
# 'jugando' <booleano para saber si el juego continúa o no>
class Juego21:
    def __init__(self):
        self.total = 0
        self.dado = Dado()
        self.jugando = True

    # Mostrará un menú simple donde se le preguntará al usuario si quiere jugar o salir del juego
    def menu(self):
        state = input("Ingresa 'jugar' para empezar el juego o 'salir' para salir del juego: ").lower()
        while state not in ['jugar', 'salir']:
            print("Respuesta no válida. Por favor, ingresa 'jugar' o 'salir'.")
            state = input("Ingresa 'jugar' para empezar el juego o 'salir' para terminar: ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        if state == 'jugar':
            self.start_game()
        elif state == 'salir':
            self.jugando = False
            print("Juego terminado. ¡Gracias por jugar!")

    # En esta clase se inicia todo el juego, es la parte principal del juego
    # Inicializa una lista la cuál va almacenar los números obtenidos al lanzar el dado
    def start_game(self):
        numbers=[]
        print("--------------------------------------------- \n ¡Bienvenido al juego 21! \n --------------------------------------------- ")
        
        # Este bucle será el encargado de lanzar el dado, almacenar los números obtenidos y verificar que el jugador cumple con las reglas del juego
        # El bucle continuará mientras el jugador decida seguir jugando
        # En caso el jugador supere los 21 puntos, te termina el juego automáticamente
        # En caso el jugador decida no seguir jugando, se termina el juego, se muestran los resultados y el método 'result' determina si el jugador ganó o perdió
        while self.jugando:
            num = self.dado.lanzar()
            numbers.append(num)
            self.total += num
            print(f"> Has lanzado el dado y obtuviste: {num}")
            print(f"> Tu total actual es: {self.total}")
            print(f"> Números almacenados: {numbers}")
            if self.verify_21():
                break
            else:
                state = input("¿Quieres seguir lanzando el dado? (si/no): ").lower()
                while state not in ['si', 'no']:
                    print("Respuesta no válida. Por favor, ingresa 'si' o 'no'.")
                    state = input("¿Quieres seguir lanzando el dado? (si/no): ").lower()
                
                if state == 'no':
                    self.jugando = False
                    print("Has decidido no seguir lanzando el dado. Fin del juego.")
                    rslt = self.result()
                    print(rslt)

    def verify_21(self):
        if self.total > 21:
            print("Tu total es mayor a 21, has perdido y ya no puedes continuar.")
            self.jugando = False
            return True
        else:
            return False

    def result(self):
        print(" -------------------------------------------- \n Mostrando resultados... \n -------------------------------------------- ")
        if self.total == 21:
            return "¡Felicidades! Has ganado con un total de 21 puntos."
        elif self.total > 21:
            return "Lo siento, has perdido. Tu total supera los 21 puntos."
        else:
            next_num = self.dado.lanzar()
            print(f"El siguiente número era: {next_num}")
            if self.total + next_num > 21:
                return f"¡Felicidades! Has ganado, tu suma total habría sido {self.total + next_num} que es mayor a 21."
            elif self.total + next_num <= 21:
                return f"Lo siento, has perdido, tu suma total habría sido {self.total + next_num} que es menor o igual a 21."

def main():
    juego = Juego21()
    playing = True
    while playing:
        juego.menu()
        print(" \n -------------------------------------------- \n")
        continue_play = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        while continue_play not in ['si', 'no']:
            print("Respuesta no válida. Por favor, ingresa 'si' o 'no'.")
            continue_play = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        if continue_play == 'no':
            playing = False
            print("Gracias por jugar. ¡Hasta la próxima!")
        elif continue_play == 'si':
            print("Reiniciando el juego...")
            # Limpiar pantalla
            os.system('cls' if os.name == 'nt' else 'clear')
            juego = Juego21()
            # juego.jugando = True
            # juego.total = 0

if __name__ == "__main__":
    main()