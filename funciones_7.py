'''
## 7. Función recursiva para invertir una cadena
Escribir `invertir(cadena)` sin usar slicing (`[::-1]`) ni estructuras avanzadas.
Debe usar recursión.
'''

def invertir(cadena):
    if cadena == "":
        return ""
    return invertir(cadena[1:]) + cadena[0]


texto = input("Cadena: ")
print(f"Invertida: {invertir(texto)}")

'''
Cómo funciona:

Caso base: si la cadena está vacía, retorna una cadena vacía. Sin él, la recursión nunca terminaría. [Cierto]
Paso recursivo: separa el primer carácter (cadena[0]), invierte el resto (cadena[1:]) y pone ese primer carácter al final. [Cierto]
Recorrido con hola: invertir("hola") = invertir("ola") + "h" = (invertir("la") + "o") + "h" = ((invertir("a") + "l") + "o") + "h" = "a" + "l" + "o" + "h" = "aloh". [Cierto]
'''