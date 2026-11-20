'''
## Enunciado 3: Suma de la diagonal principal
Elabore un programa en Python que reciba una matriz cuadrada (mismo número de filas
y columnas) ingresada por el usuario y calcule la suma de los elementos ubicados en
la diagonal principal. El programa debe imprimir la matriz completa y el valor de
la suma obtenida.
**Consideraciones:**
- Valide que la matriz ingresada sea cuadrada; en caso contrario, muestre un
mensaje de error.
- Recuerde que la diagonal principal está formada por los elementos donde el índice
de fila es igual al índice de columna.
'''

filas = 0
while filas <= 0:
    texto = input("Filas: ")
    if texto.isdigit():
        filas = int(texto)
    if filas <= 0:
        print("  Debe ser un entero mayor que cero.")

columnas = 0
while columnas <= 0:
    texto = input("Columnas: ")
    if texto.isdigit():
        columnas = int(texto)
    if columnas <= 0:
        print("  Debe ser un entero mayor que cero.")

if filas != columnas:
    print("Error: la matriz debe ser cuadrada (mismo número de filas y columnas).")
else:
    A = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f"  A[{i}][{j}]: ")))
        A.append(fila)

    suma = 0
    for i in range(filas):
        suma += A[i][i]

    ancho = 0
    for i in range(filas):
        for j in range(columnas):
            if len(str(A[i][j])) > ancho:
                ancho = len(str(A[i][j]))

    print("Matriz completa:")
    for i in range(filas):
        linea = ""
        for j in range(columnas):
            texto = str(A[i][j])
            while len(texto) < ancho + 2:
                texto = " " + texto
            linea += texto
        print(linea)

    print(f"Suma de la diagonal principal: {suma}")

'''
Enunciado 3: Suma de la diagonal principal
Pide filas y columnas y compara: si son distintas, error y termina.
Si es cuadrada, lee la matriz.
La diagonal principal son los elementos donde fila y columna coinciden: A[0][0], A[1][1], A[2][2]... Un solo bucle for i con suma += A[i][i] basta. [Cierto]
Imprime la matriz y la suma.
'''