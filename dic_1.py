'''
### Ejercicio 1: Agenda telefónica
**Enunciado:**
Solicitar nombres y teléfonos y almacenarlos en un diccionario hasta que el usuario
escriba "fin".
**Explicación:**
Cada nombre será una clave y cada teléfono su valor.
'''

agenda = {}

while True:
    nombre = input("Nombre (o 'fin' para terminar): ")
    if nombre == "fin" or nombre=="FIN":
        break
    telefono = input("Teléfono: ")
    agenda[nombre] = telefono

print(agenda)

'''
Cómo funciona:

agenda[nombre] = telefono crea la clave si no existe, o reemplaza el teléfono si el nombre ya estaba. Si repites un nombre, se pierde el teléfono anterior. [Cierto]
El teléfono se guarda como texto ('123'), sin int(...), porque la salida esperada lo muestra entre comillas. Además un teléfono puede empezar con 0 o llevar +, y como número perdería eso. [Cierto]
while True con break repite hasta que se escribe fin. [Cierto]
'''