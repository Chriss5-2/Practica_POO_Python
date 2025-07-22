import sys

main = sys.argv[1] if len(sys.argv) > 1 else print("Seleccionar un argumento: 'Enteros', 'Flotantes' or 'Complejos' \n --------- \n - Añade el argumento al ejecutar el script \n --------- \n Forma: python numbers.py <Enteros/Flotantes/Complejos>")

# Números enteros
class Entero:
    def __init__(self):
        self.num=10

            # Definición de números enteros en diferentes bases
    def decimal(self):
        # Decimal
        print("Base 10")
        a=5
        return f'{a} \n =========='

    def octal(self):
        # Octal
        print("Base 8")
        b=0o454312 # 153 802 en decimal
        return f'{b} \n =========='

    def hexadecimal(self):
        # Hexadecimal
        print("Base 16")
        c=0xac4d # 44 109 en decimal
        return f'{c} \n =========='

    def binario(self):
        # Binario
        print("Base 2")
        d=0b1010  # 10 en decimal
        return f'{d} \n =========='

            # Conversión de tipos de datos numéricos
    def str_to_int(self):
        # Convertir un string a entero
        print("Convertir string a entero")
        num_string = "1234"
        num_entero= int(num_string)
        return f'{num_entero} \n =========='

    def int_to_str(self):
        # Convertir un entero a string
        print("Convertir entero a string")
        num_entero_2 = 1234
        num_string_2 = str(num_entero_2)
        return f'{num_string_2} \n =========='

            # Cambio de base numérica
    def int_to_bin(self):
        # Convertir un entero a binario
        print("Convertir entero a binario")
        num_binario = bin(self.num)  # '0b1010'
        return f'{num_binario} \n =========='

    def int_to_oct(self):
        # Convertir un entero a octal
        print("Convertir entero a octal")
        num_octal = oct(self.num)  # '0o12'
        return f'{num_octal} \n =========='

    def int_to_hex(self):
        # Convertir un entero a hexadecimal
        print("Convertir entero a hexadecimal")
        num_hexadecimal = hex(self.num)  # '0xa'
        return f'{num_hexadecimal} \n =========='

            # Tipo de Dato
    def type_of_data(self):
        # Verificar tipo de dato
        print("Tipo de dato")
        ty_a=type(self.num)  # <class 'int'
        return f'{ty_a} \n =========='

def main_1():
    print("Números enteros")
    numero=Entero()
    print(numero.decimal())
    print(numero.octal())
    print(numero.hexadecimal())
    print(numero.binario())
    print(numero.str_to_int())
    print(numero.int_to_str())
    print(numero.int_to_bin())
    print(numero.int_to_oct())


class Float:
    def __init__(self):
        self.num=10.5

    def float(self):
        # Definición de números flotantes
        print("Números flotantes")
        a=10.5
        return f'{a} \n =========='

    def division_result_float(self):
        # División de enteros: resultado flotante
        print("División de enteros: resultado flotante")
        a=10
        b=4
        resultado=a/b
        return f'{resultado} \n =========='
        return type(resultado)

    def division_result_int(self):
        # División de enteros: resultado entero
        print("División de enteros: resultado entero")
        a=10
        b=4
        resultado=a//b
        return f'{resultado} \n =========='
        return type(resultado)
    
    def double_division(self):
        # Doble división de enteros: Resultado <int>
        print("Doble división de enteros: Resultado <int>")
        a=10
        b=4
        resultado=a//b
        return f'{resultado} \n =========='
        return type(resultado)
        # La doble división de enteros es un entero
        # La doble división da como resultado el cociente entero de la división

    def convert_int_to_float(self):
        # Convertir un entero a flotante
        print("Convertir un entero a flotante")
        num_entero = 10
        num_flotante = float(num_entero)
        return f'{num_flotante} \n =========='
        return type(num_flotante)

    def cientific_notation_entero(self):
        # Notación científica: es un número en forma de a * 10^b
        # El resultado es un número de tipo float
        print("Notación científica")
        num_cientifico = 1.5e3 # 1.5 * 10^3
        return f'{num_cientifico} \n =========='
        return type(num_cientifico)
    
    def cientific_notation_decimal(self):
        # Notación científica: es un número en forma de a * 10^b
        # El resultado es un número de tipo float
        print("Notación científica con decimal")
        num_cientifico_decimal = 1.5e-3 # 1.5 * 10^-3
        return f'{num_cientifico_decimal} \n =========='
        return type(num_cientifico_decimal)

    def float_point(self):
        # Error de punto flotante al realizar operaciones
        print("Error de punto flotante")
        a = 0.1
        b = 0.2
        resultado = a + b
        return f'{resultado} \n =========='
        # El resultado es 0.30000000000000004 en lugar de 0.3
        return type(resultado)

    # Notamos que en la división de dos enteros, el resultado es entero pero sigue siendo tipo float
    # Todas las divisiones dan un resultado de tipo float

def main_2():
    print("Números flotantes")
    numero=Float()
    print(numero.float())
    print(numero.division_result_float())
    print(numero.division_result_int())
    print(numero.double_division())
    print(numero.convert_int_to_float())
    print(numero.cientific_notation_entero())
    print(numero.cientific_notation_decimal())
    print(numero.float_point())


class Complex:
    # General form: ax + bi
    # real part: a
    # imaginary part: b
    # j = sqrt(-1)
    def __init__(self):
        self.num_1 = 3 + 4j
        self.num_2 = 1 - 2j

    def complex_number(self):
        # Definición de números complejos
        # El resultado es un número de tipo complex
        print("Números complejos")
        a = 3 + 4j
        return f'{a} \n =========='
        return type(a)

    def sum_complex(self):
        # Suma de números complejos
        print("Suma de números complejos")
        resultado = self.num_1 + self.num_2
        return f'{resultado} \n =========='
        return type(resultado)

    def squared_complex(self):
        # Elevación al cuadrado de un número complejo
        print("Elevación al cuadrado de un número complejo")
        resultado = self.num_1 ** 2
        return f'{resultado} \n =========='
        return type(resultado)

    def conjugate_complex(self):
        # Conjugado de un número complejo
        print("Conjugado de un número complejo")
        resultado = self.num_1.conjugate()
        return f'{resultado} \n =========='
        return type(resultado)

    def multiply_complex(self):
        # Multiplicación de números complejos
        print("Multiplicación de números complejos")
        resultado = self.num_1 * self.num_2
        return f'{resultado} \n =========='
        return type(resultado)

    def obtain_real_part(self):
        # Obtener la parte real de un número complejo
        # El resultado es un número de tipo float
        print(f"Obtener la parte real de {self.num_1}")
        resultado = self.num_1.real
        return f'{resultado} \n =========='
        return type(resultado)
    
    def obtain_imaginary_part(self):
        # Obtener la parte imaginaria de un número complejo
        # El resultado es un número de tipo float
        print(f"Obtener la parte imaginaria de {self.num_1}")
        resultado = self.num_1.imag
        return f'{resultado} \n =========='
        return type(resultado)

def main_3():
    print("Números complejos")
    numero=Complex()
    print(numero.complex_number())
    print(numero.sum_complex())
    print(numero.squared_complex())
    print(numero.conjugate_complex())
    print(numero.multiply_complex())
    print(numero.obtain_real_part())
    print(numero.obtain_imaginary_part())

    

if __name__ == "__main__":
    if main == "Enteros":
        main_1()
    elif main == "Flotantes":
        main_2()
    elif main == "Complejos":
        main_3()