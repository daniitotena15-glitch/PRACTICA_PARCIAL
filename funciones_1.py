'''
## 1. Función para calcular el factorial de un número
Definir una función `factorial(n)` que reciba un entero positivo y retorne su
factorial.
Toda la lógica debe estar dentro de la función.
'''

def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


n = int(input("Número: "))

if n < 0:
    print("Error: el número debe ser positivo.")
else:
    print(f"Salida: {factorial(n)}")

'''
Cómo funciona:

resultado empieza en 1, que es el valor neutro de la multiplicación. [Cierto]
El bucle multiplica por cada número de 2 a n: 1 × 2 × 3 × 4 × 5 = 120. Empieza en 2 porque multiplicar por 1 no cambia nada. [Cierto]
Con n = 0 el bucle no se ejecuta y retorna 1, que es correcto porque 0! = 1. [Cierto]
La validación n < 0 va fuera de la función para que factorial solo contenga la lógica del cálculo. El enunciado dice “entero positivo”, así que 0 se acepta por ser el caso base matemático. [Probable]
'''