#Tabla de multiplicar Escribe un programa que muestre la tabla de multiplicar de un número ingresado por el usuario (del 1 al 10) usando un bucle for.

numero = int(input("Introduce un número para su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")