'''
### Ejercicio 4: Diccionario invertido
**Enunciado:**
Invertir un diccionario de clave→valor a valor→clave.
**Explicación:**
Usar comprensión de diccionarios `{v: k for k, v in dic.items()}`.
'''
dic = {}

while True:
    clave = input("Clave (o 'fin' para terminar): ")
    if clave == "fin" or clave=="FIN":
        break
    dic[clave] = int(input(f"Valor de {clave}: "))

invertido = {v: k for k, v in dic.items()}

print(invertido)

'''
Cómo funciona:

dic.items() devuelve los pares (clave, valor), y for k, v in ... los desempaqueta en dos variables. [Cierto]
{v: k ...} crea cada par nuevo con el valor como clave y la clave como valor. [Cierto]
'''