#Pide dos números e indica cuál es mayor o si son iguales.

num1 = int(input("ingrese un número: "))
num2 = int(input("ingrese un número: "))

if num1 > num2:
    print(f"el primer digito {num1} es mayor")
elif num1 < num2:
    print(f"el segundo digito {num2} es mayor")
else:
    print("los numeros son iguales")