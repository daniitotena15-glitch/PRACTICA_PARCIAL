'''
### Ejercicio 5: Fusionar diccionarios
**Enunciado:**
Combinar dos diccionarios en uno solo. Si hay claves repetidas, el segundo debe
sobrescribir al primero.
**Explicación:**
Usar el método `update()` o el operador `|` (Python 3.9+).
'''

A = {}
B = {}

print("Diccionario A:")
while True:
    clave = input("  Clave (o 'fin' para terminar): ")
    if clave == "fin" or clave=="FIN":
        break
    A[clave] = int(input(f"  Valor de {clave}: "))

print("Diccionario B:")
while True:
    clave = input("  Clave (o 'fin' para terminar): ")
    if clave == "fin" or clave=="FIN":
        break
    B[clave] = int(input(f"  Valor de {clave}: "))

fusionado = A.copy()
fusionado.update(B)

print(fusionado)

'''
Cómo funciona:

La clave 'y' existe en los dos diccionarios. Como B se aplica después, su valor (10) reemplaza al de A (2). [Cierto]
El orden importa: B | A daría {'y': 2, ...}, porque entonces A sobrescribiría a B. [Cierto]
El orden de las claves en el resultado es x, y, z: las claves de A conservan su posición y las nuevas de B se añaden al final. [Cierto]
'''