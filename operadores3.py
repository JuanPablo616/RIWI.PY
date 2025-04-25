#Calcula el residuo de dividir dos números dados por el usuario.

dividendo = int(input("ingrese el dividendo: "))
divisor = int(input("ingrese el divisor :"))

residuo = dividendo % divisor

print(f"el residuo de la division de {dividendo}, entre {divisor} es: {residuo}")