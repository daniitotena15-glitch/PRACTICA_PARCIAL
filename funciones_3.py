'''
## 3. Función que determine si un número es primo
Definir `es_primo(n)` que retorne `True` o `False`.
Debe verificar divisibilidad desde 2 hasta la raíz cuadrada de n.
'''

def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input("Número: "))

if es_primo(n):
    print(f"{n} es primo")
else:
    print(f"{n} no es primo")

'''
Cómo funciona:

n < 2 descarta 0, 1 y los negativos, que no son primos por definición. [Cierto]
El bucle prueba divisores desde 2 mientras i * i <= n. Si n tuviera un divisor mayor que su raíz, también tendría uno menor que la raíz, así que no hace falta revisar más allá. [Cierto]
n % i == 0 significa que i divide a n exactamente. En cuanto aparece uno, retorna False y la función termina sin seguir probando. [Cierto]
Si el bucle termina sin encontrar divisores, retorna True. [Cierto]
'''