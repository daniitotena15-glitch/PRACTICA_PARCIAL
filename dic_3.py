'''
### Ejercicio 3: Promedio de calificaciones
**Enunciado:**
Ingresar nombres de estudiantes y sus notas, y calcular el promedio general.
**Explicación:**
Almacenar pares nombre→nota y usar `sum()` y `len()` sobre `dict.values()`.
'''

notas = {}

while True:
    nombre = input("Nombre del estudiante (o 'fin' para terminar): ")
    if nombre == "fin" or nombre=="FIN":
        break
    notas[nombre] = float(input(f"Nota de {nombre}: "))

if len(notas) == 0:
    print("No ingresó ningún estudiante.")
else:
    promedio = sum(notas.values()) / len(notas)
    print(f"Promedio general: {promedio}")

'''
Cómo funciona:

notas[nombre] = float(...) guarda cada nota como número, no como texto, porque hay que sumarla. [Cierto]
sum(notas.values()) suma todas las notas: 4.0 + 3.5 + 4.5 = 12.0. [Cierto]
len(notas) cuenta los estudiantes (3), y 12.0 / 3 = 4.0. [Cierto]
El if len(notas) == 0 evita dividir entre 0 si el usuario escribe fin de inmediato. [Cierto]
'''