'''
## Enunciado 4: Búsqueda del mayor valor y su posición
Elabore un programa en Python que reciba una matriz de tamaño *n* x *m* ingresada
por el usuario y determine el valor mayor contenido en ella, así como la fila y
columna en la que se encuentra (posición). El programa debe imprimir la matriz, el
valor máximo encontrado y su posición.
**Consideraciones:**
- Si el valor máximo se repite en más de una posición, el programa debe reportar
únicamente la primera posición donde lo encuentra.
- La posición debe mostrarse en el formato: fila X, columna Y.
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

A = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(int(input(f"  A[{i}][{j}]: ")))
    A.append(fila)

# Solo se actualiza con ">" para quedarse con la primera posición
maximo = A[0][0]
pos_fila = 0
pos_columna = 0
for i in range(filas):
    for j in range(columnas):
        if A[i][j] > maximo:
            maximo = A[i][j]
            pos_fila = i
            pos_columna = j

ancho = 0
for i in range(filas):
    for j in range(columnas):
        if len(str(A[i][j])) > ancho:
            ancho = len(str(A[i][j]))

print("Matriz:")
for i in range(filas):
    linea = ""
    for j in range(columnas):
        texto = str(A[i][j])
        while len(texto) < ancho + 2:
            texto = " " + texto
        linea += texto
    print(linea)

print(f"Valor máximo: {maximo}")
print(f"Posición: fila {pos_fila + 1}, columna {pos_columna + 1}")

'''
Enunciado 4: Mayor valor y su posición
Lee dimensiones y matriz.
Toma A[0][0] como máximo provisional, con posición (0, 0).
Recorre toda la matriz fila por fila. Si un elemento es estrictamente mayor (>) que maximo, actualiza el máximo y su posición. [Cierto]
Como solo cambia con > y no con >=, si el máximo se repite, se queda la primera posición encontrada. [Cierto]
Imprime la matriz, el máximo y la posición sumando 1 a los índices (pos_fila + 1), porque el enunciado habla de “fila X, columna Y” como las contaría una persona.
'''