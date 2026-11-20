'''
## Enunciado 2: Matriz transpuesta
Elabore un programa en Python que reciba una matriz de tamaño *n* x *m* ingresada
por el usuario y calcule su matriz transpuesta (donde las filas se convierten en
columnas y viceversa). El programa debe imprimir la matriz original y la matriz
transpuesta.
**Consideraciones:**
- La matriz de entrada no necesariamente debe ser cuadrada.
- La matriz transpuesta resultante tendrá dimensiones *m* x *n*.
'''

n = 0
while n <= 0:
    texto = input("Filas (n): ")
    if texto.isdigit():
        n = int(texto)
    if n <= 0:
        print("  Debe ser un entero mayor que cero.")

m = 0
while m <= 0:
    texto = input("Columnas (m): ")
    if texto.isdigit():
        m = int(texto)
    if m <= 0:
        print("  Debe ser un entero mayor que cero.")

A = []
for i in range(n):
    fila = []
    for j in range(m):
        fila.append(int(input(f"  A[{i}][{j}]: ")))
    A.append(fila)

# Transpuesta de m x n
transpuesta = []
for j in range(m):
    fila = []
    for i in range(n):
        fila.append(A[i][j])
    transpuesta.append(fila)

# Se imprime dos veces con el mismo bloque: etapa 0 = original, etapa 1 = transpuesta
for etapa in range(2):
    if etapa == 0:
        matriz = A
        filas_m = n
        columnas_m = m
        print("Matriz original:")
    else:
        matriz = transpuesta
        filas_m = m
        columnas_m = n
        print("Matriz transpuesta:")

    ancho = 0
    for i in range(filas_m):
        for j in range(columnas_m):
            if len(str(matriz[i][j])) > ancho:
                ancho = len(str(matriz[i][j]))

    for i in range(filas_m):
        linea = ""
        for j in range(columnas_m):
            texto = str(matriz[i][j])
            while len(texto) < ancho + 2:
                texto = " " + texto
            linea += texto
        print(linea)

'''
Enunciado 2: Matriz transpuesta
Lee n (filas) y m (columnas) y la matriz A.
La transpuesta tiene m filas y n columnas. El bucle externo recorre j (columnas de A) y el interno i (filas de A). Cada fila nueva es una columna completa de A: A[0][j], A[1][j], .... [Cierto]
Para imprimir dos matrices sin funciones, se usa for etapa in range(2). En la etapa 0 se asignan matriz = A con dimensiones n × m; en la etapa 1, matriz = transpuesta con dimensiones m × n. El mismo bloque de impresión sirve para las dos. [Cierto]
'''