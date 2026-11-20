'''
### Ejercicio 2: Contador de palabras
**Enunciado:**
Solicitar una frase y contar cuántas veces aparece cada palabra.
**Explicación:**
Usar un diccionario donde las claves son las palabras y los valores sus
frecuencias.
'''

frase = input("Frase: ") + " "

frecuencias = {}
palabra = ""

for c in frase:
    if c == " ":
        if palabra != "":
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
            palabra = ""
    else:
        palabra += c

print(frecuencias)

'''
Cómo funciona:

Se va acumulando cada letra en palabra. Al llegar a un espacio, la palabra está completa y se cuenta. [Cierto]
El + " " del inicio garantiza que la última palabra también se cuente, porque la frase no termina en espacio. [Cierto]
if palabra != "" evita contar palabras vacías cuando hay espacios dobles o la frase empieza con espacio. [Cierto]
Si la palabra ya es clave, se suma 1; si no, se crea con valor 1. La versión corta de esas cuatro líneas es frecuencias[palabra] = frecuencias.get(palabra, 0) + 1. [Cierto]
'''