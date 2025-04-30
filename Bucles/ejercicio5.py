#Adivina el número Crea un programa que genere un número aleatorio entre 1 y 10, y le pida al usuario que lo adivine. El programa debe indicar si el número ingresado es mayor, menor o correcto. El usuario tiene hasta 3 intentos.

import random
intentos = 3
aleatorio = random.randint(1,10)
print("adivina el numero entre 1-10, tienes 3 intentos: ")

while intentos > 0:
    intento = int(input("introduce tu número: "))
    if intento == aleatorio:
        print("Felicidades, adivinaste el número")
        break
    elif intento < aleatorio:
        print("el numero es mayor.")
    else:
        print("el numero es menor.")
    intento -= 1
    if intentos == 0:
        print(f"No has adivinado el número, el número era: {aleatorio}")