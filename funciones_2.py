'''
## 2. Calculadora con funciones independientes
Crear funciones independientes:
- `sumar(a, b)`
- `restar(a, b)`
- `multiplicar(a, b)`
- `dividir(a, b)`
Luego una función `calculadora()` debe pedir los datos y llamar a la función
adecuada.
'''

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None
    return a / b


def calculadora():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    operacion = input("Operación (+, -, *, /): ")

    if operacion == "+":
        resultado = sumar(a, b)
    elif operacion == "-":
        resultado = restar(a, b)
    elif operacion == "*":
        resultado = multiplicar(a, b)
    elif operacion == "/":
        resultado = dividir(a, b)
        if resultado is None:
            print("Error: no se puede dividir entre cero.")
            return
    else:
        print("Operación no válida.")
        return

    if resultado == int(resultado):
        resultado = int(resultado)
    print(f"Resultado: {resultado}")


calculadora()

'''
Cómo funciona:

Las cuatro funciones son independientes: cada una recibe a y b y retorna el resultado, sin pedir datos ni imprimir. [Cierto]
calculadora() pide los datos, decide con if/elif qué función llamar y muestra el resultado. Toda la interacción con el usuario queda ahí. [Cierto]
dividir retorna None cuando b es 0, y calculadora lo detecta con is None. Se usa None y no 0 porque 0 también es un resultado válido (por ejemplo 0 / 5). [Cierto]
Se usa float para aceptar decimales. El bloque final convierte a entero cuando el resultado no tiene parte decimal, para mostrar 4 en lugar de 4.0. [Cierto]
'''