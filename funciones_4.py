'''
## 4. Función para convertir grados Celsius a Fahrenheit
Definir `celsius_fahrenheit(c)` aplicando la fórmula:
F = (C × 9/5) + 32
'''

def celsius_fahrenheit(c):
    return (c * 9 / 5) + 32


c = float(input("Grados Celsius: "))
f = celsius_fahrenheit(c)

print(f"{c} °C = {f} °F")

'''
Cómo funciona:

La función solo aplica la fórmula y retorna el resultado, sin pedir datos ni imprimir. [Cierto]
c * 9 / 5 es lo mismo que c * (9/5): Python evalúa de izquierda a derecha y el resultado es idéntico. [Cierto]
Se usa float para aceptar temperaturas con decimales, como 36.6. [Cierto]
'''