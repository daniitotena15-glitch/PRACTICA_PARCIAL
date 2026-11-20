'''
## Enunciado 1: Suma de dos matrices
Elabore un programa en Python que reciba dos matrices de igual tamaño (número de
filas y columnas) ingresadas por el usuario, y calcule la matriz resultante de
sumar elemento a elemento ambas matrices. El programa debe imprimir la matriz
resultante con un formato ordenado (filas y columnas alineadas).
**Consideraciones:**
- Solicite primero el número de filas y columnas.
- Valide que ambas matrices tengan las mismas dimensiones antes de sumarlas.
- Muestre un mensaje de error si las dimensiones no coinciden.
'''

# Dimensiones de A
filas_a = 0
while filas_a <= 0:
    texto = input("Filas de A: ")
    if texto.isdigit():
        filas_a = int(texto)
    if filas_a <= 0:
        print("  Debe ser un entero mayor que cero.")

columnas_a = 0
while columnas_a <= 0:
    texto = input("Columnas de A: ")
    if texto.isdigit():
        columnas_a = int(texto)
    if columnas_a <= 0:
        print("  Debe ser un entero mayor que cero.")

# Dimensiones de B
filas_b = 0
while filas_b <= 0:
    texto = input("Filas de B: ")
    if texto.isdigit():
        filas_b = int(texto)
    if filas_b <= 0:
        print("  Debe ser un entero mayor que cero.")

columnas_b = 0
while columnas_b <= 0:
    texto = input("Columnas de B: ")
    if texto.isdigit():
        columnas_b = int(texto)
    if columnas_b <= 0:
        print("  Debe ser un entero mayor que cero.")

if filas_a != filas_b or columnas_a != columnas_b:
    print("Error: las matrices deben tener las mismas dimensiones.")
else:
    A = []
    print("Matriz A:")
    for i in range(filas_a):
        fila = []
        for j in range(columnas_a):
            fila.append(int(input(f"  A[{i}][{j}]: ")))
        A.append(fila)

    B = []
    print("Matriz B:")
    for i in range(filas_b):
        fila = []
        for j in range(columnas_b):
            fila.append(int(input(f"  B[{i}][{j}]: ")))
        B.append(fila)

    suma = []
    for i in range(filas_a):
        fila = []
        for j in range(columnas_a):
            fila.append(A[i][j] + B[i][j])
        suma.append(fila)

    # Ancho de la columna = largo del número más largo
    ancho = 0
    for i in range(filas_a):
        for j in range(columnas_a):
            if len(str(suma[i][j])) > ancho:
                ancho = len(str(suma[i][j]))

    print("Matriz resultante:")
    for i in range(filas_a):
        linea = ""
        for j in range(columnas_a):
            texto = str(suma[i][j])
            while len(texto) < ancho + 2:
                texto = " " + texto
            linea += texto
        print(linea)

'''
Enunciado 1: Suma de dos matrices
Pide filas y columnas de A y de B por separado.
Compara: si no coinciden, imprime el error y el programa termina sin pedir elementos.
Si coinciden, lee A y B.
Arma suma recorriendo cada posición (i, j) y calculando A[i][j] + B[i][j]. [Cierto]
Imprime suma alineada.
'''