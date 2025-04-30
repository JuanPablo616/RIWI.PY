#Contador regresivo Crea un programa que pida un número positivo al usuario y haga una cuenta regresiva desde ese número hasta 0 usando un bucle while.

num = int(input("introduzca un número positivo: "))
if num == 0:
        print("ingrese un número positivo")
elif num < 0:
        print("ingrese un número positivo")
else:
    while num >= 0:
        print(num)
    num -= 1 