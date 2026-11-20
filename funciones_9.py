'''
## 9. Función para calcular la potencia sin usar **
Crear `potencia(base, exponente)` usando multiplicaciones repetidas o recursión
'''

def potencia(base, exponente):
    if exponente == 0:
        return 1

    resultado = 1
    for i in range(abs(exponente)):
        resultado *= base

    if exponente < 0:
        return 1 / resultado
    return resultado


base = float(input("Base: "))
exponente = int(input("Exponente: "))

if base == 0 and exponente < 0:
    print("Error: 0 elevado a un exponente negativo no está definido.")
else:
    resultado = potencia(base, exponente)

    if resultado == int(resultado):
        resultado = int(resultado)
    print(f"Resultado: {resultado}")

'''
Cómo funciona:

resultado empieza en 1 y se multiplica por base tantas veces como indique el exponente: 2 × 2 × 2 ... diez veces da 1024. [Cierto]
exponente == 0 retorna 1 de inmediato, porque cualquier número elevado a 0 es 1. [Cierto]
Con exponente negativo, se calcula la potencia con abs(exponente) y se retorna su inverso: 2^-2 = 1 / 2^2 = 0.25. [Cierto]
El exponente se lee como int porque las multiplicaciones repetidas solo tienen sentido con exponentes enteros. Un exponente decimal (0.5) no se puede hacer con este método. [Cierto]
0 con exponente negativo se valida fuera de la función, porque dividiría entre 0. [Cierto]5
'''