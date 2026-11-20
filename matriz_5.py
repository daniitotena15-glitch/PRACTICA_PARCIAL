'''
## Enunciado 5: Multiplicación de una matriz por un escalar
Elabore un programa en Python que reciba una matriz de tamaño *n* x *m* ingresada
por el usuario y un valor escalar (número entero o decimal). El programa debe
calcular la matriz resultante de multiplicar cada uno de sus elementos por dicho
escalar, e imprimir tanto la matriz original como la matriz resultante.
**Consideraciones:**
- El escalar puede ser positivo, negativo o cero.
- Verifique que todos los valores ingresados a la matriz sean numéricos.
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

# Lectura con validación manual: signo opcional, dígitos y máximo un punto
A = []
print("Matriz A:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        valido = False
        while not valido:
            texto = input(f"  A[{i}][{j}]: ")
            valido = True
            puntos = 0
            digitos = 0
            for k in range(len(texto)):
                c = texto[k]
                if c == "-" and k == 0:
                    pass
                elif c == "." and puntos == 0:
                    puntos += 1
                elif c >= "0" and c <= "9":
                    digitos += 1
                else:
                    valido = False
            if digitos == 0:
                valido = False
            if not valido:
                print("  Valor no numérico, intente de nuevo.")
        fila.append(float(texto))
    A.append(fila)

# Escalar, misma validación
valido = False
while not valido:
    texto = input("Escalar: ")
    valido = True
    puntos = 0
    digitos = 0
    for k in range(len(texto)):
        c = texto[k]
        if c == "-" and k == 0:
            pass
        elif c == "." and puntos == 0:
            puntos += 1
        elif c >= "0" and c <= "9":
            digitos += 1
        else:
            valido = False
    if digitos == 0:
        valido = False
    if not valido:
        print("  Valor no numérico, intente de nuevo.")
escalar = float(texto)

resultado = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(A[i][j] * escalar)
    resultado.append(fila)

# Etapa 0 = original, etapa 1 = resultante
for etapa in range(2):
    if etapa == 0:
        matriz = A
        print("Matriz original:")
    else:
        matriz = resultado
        print("Matriz resultante:")

    ancho = 0
    for i in range(filas):
        for j in range(columnas):
            valor = matriz[i][j]
            if valor == int(valor):
                texto = str(int(valor))
            else:
                texto = str(round(valor, 2))
            if len(texto) > ancho:
                ancho = len(texto)

    for i in range(filas):
        linea = ""
        for j in range(columnas):
            valor = matriz[i][j]
            if valor == int(valor):
                texto = str(int(valor))
            else:
                texto = str(round(valor, 2))
            while len(texto) < ancho + 2:
                texto = " " + texto
            linea += texto
        print(linea)

'''
Enunciado 5: Multiplicación por un escalar
Lee dimensiones (mismo bloque de siempre).
Lee cada elemento con validación manual, porque no se puede usar try/except. Para cada texto ingresado:
Parte de valido = True.
Recorre los caracteres por posición k. Acepta un - solo si está en la posición 0, un . solo si es el primero que aparece (puntos == 0), y dígitos de 0 a 9. Cualquier otro carácter pone valido = False. [Cierto]
Cuenta los dígitos; si no hay ninguno (por ejemplo - o . solos), también es inválido. [Cierto]
Si es inválido, avisa y el while not valido vuelve a preguntar. Si es válido, se convierte con float(texto).
Lee el escalar con exactamente la misma validación.
Arma resultado multiplicando cada A[i][j] * escalar.
Imprime las dos matrices con el truco de etapa. Antes de medir y rellenar, cada valor se convierte a texto así: si es entero (valor == int(valor)) se muestra sin .0; si no, se redondea a 2 decimales. [Cierto]
'''