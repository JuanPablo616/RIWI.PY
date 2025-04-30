#Clasificador de números Escribe un programa que pida al usuario un número entero y determine si es positivo, negativo o cero.

num = int(input("Introduce un número entero: "))
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.") 