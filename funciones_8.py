'''
## 8. Función para determinar si una cadena es palíndroma
Crear `es_palindromo(cadena)` comparando carácter por carácter.
Puede usar la función `invertir`
'''

def invertir(cadena, i=None):
    if i is None:
        i = len(cadena) - 1
    if i < 0:
        return ""
    return cadena[i] + invertir(cadena, i - 1)


def es_palindromo(cadena):
    # Normaliza: minúsculas y sin espacios
    limpia = ""
    for c in cadena:
        if c != " ":
            limpia += c.lower()

    return limpia == invertir(limpia)


texto = input("Cadena: ")

if es_palindromo(texto):
    print("Es palíndroma")
else:
    print("No es palíndroma")

'''
Cómo funciona:

es_palindromo primero arma limpia, que es la cadena sin espacios y en minúsculas. Así Anita lava la tina se compara como anitalavalatina. [Cierto]
Luego compara limpia con invertir(limpia). Si son iguales, se lee igual al derecho y al revés. [Cierto]
Usa == entre textos, que compara carácter por carácter internamente. [Cierto]
'''