'''
### Ejercicio 3: Matriz identidad
**Enunciado:**
Solicitar un número `n` y construir una **matriz identidad** de tamaño `n×n`.
**Explicación:**
Una matriz identidad tiene 1s en la diagonal principal y 0s en las demás
posiciones.
'''
n = int(input("n = "))

matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

for fila in matriz:
    print(fila)

'''
i es el número de fila y j el de columna. Los 1s van donde i == j, que es justo la diagonal principal. [Cierto]
El bucle interno arma cada fila y el externo las junta en matriz. [Cierto]
print(fila) imprime cada lista con el formato [1, 0, 0] que pide la salida esperada. [Cierto]
'''