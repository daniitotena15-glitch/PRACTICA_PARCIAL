'''
### Ejercicio 4: Suma de dos matrices
**Enunciado:**
Dadas dos matrices del mismo tamaño, calcular su suma elemento a elemento.
**Explicación:**
Cada posición (i, j) se suma entre las dos matrices.
'''

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

A = []
print("Matriz A:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(int(input(f"  A[{i}][{j}]: ")))
    A.append(fila)

B = []
print("Matriz B:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(int(input(f"  B[{i}][{j}]: ")))
    B.append(fila)

suma = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(A[i][j] + B[i][j])
    suma.append(fila)

print(suma)

'''
Cómo funciona:

La posición (i, j) de la suma es A[i][j] + B[i][j]. Ambas matrices usan las mismas filas y columnas, así que no hace falta validar que el tamaño coincida. [Cierto]
Uso int porque la salida esperada muestra enteros. Si necesitas decimales, cambia int(...) por float(...). [Cierto]
print(suma) imprime la lista de listas con el formato [[6, 8], [10, 12]]. [Cierto]
'''