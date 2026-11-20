'''
## 5. Función para obtener el máximo de tres números
Escribir `maximo_de_tres(a, b, c)` sin usar listas ni la función `max()`.
'''

def maximo_de_tres(a, b, c):
    maximo = a
    if b > maximo:
        maximo = b
    if c > maximo:
        maximo = c
    return maximo


a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))

resultado = maximo_de_tres(a, b, c)

if resultado == int(resultado):
    resultado = int(resultado)

print(f"El máximo es: {resultado}")

'''
Cómo funciona:

maximo empieza con a como máximo provisional. [Cierto]
Si b es mayor, lo reemplaza; luego si c es mayor que el máximo actual, lo reemplaza. Al final queda el mayor de los tres. [Cierto]
Compara c contra maximo y no contra a: si se comparara contra a, un caso como a = 1, b = 9, c = 5 devolvería 5 en lugar de 9. [Cierto]
No usa listas ni max(), como pide el enunciado. [Cierto]
Funciona con negativos e iguales: con -3, -7, -5 retorna -3, y con 5, 5, 5 retorna 5. [Cierto]
'''