'''
### Ejercicio 5: Transposición de una matriz
**Enunciado:**
Generar la **matriz transpuesta** de una matriz ingresada por el usuario.
**Explicación:**
Se intercambian filas por columnas: `A[i][j] → A[j][i]`.
'''

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

A = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(int(input(f"  A[{i}][{j}]: ")))
    A.append(fila)

transpuesta = []
for j in range(columnas):
    fila = []
    for i in range(filas):
        fila.append(A[i][j])
    transpuesta.append(fila)

print(transpuesta)

'''
Cómo funciona:

La transpuesta tiene columnas filas y filas columnas. Por eso el bucle externo recorre j (columnas de A) y el interno recorre i (filas de A). [Cierto]
Cada fila nueva se arma tomando A[i][j] con j fijo y i variando, es decir, una columna completa de A. [Cierto]
Si la matriz no es cuadrada (como aquí, 2×3), la transpuesta cambia de tamaño (3×2). Un error común es recorrer ambos bucles con filas, lo que falla con matrices no cuadradas. [Cierto]
'''