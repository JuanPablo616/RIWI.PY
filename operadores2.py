#Dado un precio y un porcentaje de descuento, muestra el valor final a pagar.
precio = int(input("ingrese el valor del producto: "))
descuento = int(input("ingrese el descuento total: "))

desctot = precio * (descuento/100)

totalPagar = precio - desctot

print(f"el valor total a pagar es: ${totalPagar}")