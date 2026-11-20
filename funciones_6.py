'''
## 6. Función que cuente los dígitos de un número
Crear la función `contar_digitos(n)` que retorne cuántos dígitos tiene un número
entero.
'''

def contar_digitos(n):
    if n < 0:
        n = -n
    if n == 0:
        return 1
    cantidad = 0
    while n > 0:
        n //= 10
        cantidad += 1
    return cantidad


n = int(input("Número: "))
print(f"Cantidad de dígitos: {contar_digitos(n)}")

'''
Cómo funciona:

n //= 10 es la división entera entre 10: quita la última cifra (12345 pasa a 1234). Cada vez que se quita una, cantidad sube en 1. Cuando n llega a 0, ya se contaron todas. [Cierto]
n < 0 lo convierte en positivo, para que -123 también dé 3 y el signo no cuente como dígito. [Cierto]
n == 0 se trata aparte: sin esa línea el bucle no se ejecutaría y retornaría 0, pero el número 0 tiene 1 dígito. [Cierto]
No usa listas ni len(str(n)), así que toda la lógica es aritmética. [Cierto]
'''