'''
## 10. Función que calcule el mínimo común múltiplo (mcm)
Crear dos funciones:
1. `mcd(a, b)` usando el algoritmo de Euclides.
2. `mcm(a, b)` usando la fórmula:
mcm(a, b) = |a * b| / mcd(a, b)
'''

def mcd(a, b):
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)


a = int(input("Primer número: "))
b = int(input("Segundo número: "))

print(f"MCD: {mcd(a, b)}")
print(f"MCM: {mcm(a, b)}")

'''
Cómo funciona:

Euclides: el MCD de a y b es el mismo que el de b y a % b. Se repite hasta que b llega a 0, y entonces a es el MCD. [Cierto]
Recorrido con 12 y 18: (12, 18) pasa a (18, 12), luego a (12, 6), luego a (6, 0). Retorna 6. [Cierto]
a, b = b, a % b asigna las dos variables a la vez, sin necesitar una variable temporal. [Cierto]
abs(...) al inicio de mcd hace que funcione con negativos, y el abs(a * b) de mcm implementa el valor absoluto de la fórmula. [Cierto]
Se usa // (división entera) y no /, porque a * b siempre es divisible entre el mcd, y así el resultado queda como entero y no como 36.0. [Cierto]
mcm retorna 0 si alguno de los números es 0 antes de llamar a mcd. Sin esa línea, mcm(0, 0) dividiría entre mcd(0, 0) = 0 y lanzaría ZeroDivisionError. [Cierto]
'''