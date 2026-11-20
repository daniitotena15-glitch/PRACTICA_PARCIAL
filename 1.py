n = int(input("¿Cuántos números va a ingresar? "))

numeros = []
for i in range(n):
    numeros.append(float(input(f"Número {i + 1}: ")))

if n == 0:
    print("No ingresó ningún número.")
else:
    promedio = sum(numeros) / n

    mayores = []
    for x in numeros:
        if x > promedio:
            mayores.append(int(x) if x.is_integer() else x)
    mayores.sort()

    print(f"Promedio: {promedio}")
    print(f"Mayores que el promedio: {mayores}")