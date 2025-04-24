def total():
    producto = input("ingrese el nombre del producto: ")

    while True: #validamos que el usuario si digite un valor correcto.
        try:
            precioUnitario = float(input("ingrese el precio del producto: "))
            if precioUnitario < 0:
                print("Valor invalido, intentelo de nuevo.")
            else:
                break
        except ValueError:
            print("por favor, ingrese el valor correcto.")

    while True: #validamos que el usuario digite una cantidad correcta.
        try:
            cantidad = int( input("ingresa la cantidad de productos: "))
            if cantidad < 1:
                print("cantidad no valida, intente de nuevo")
            else:
                break
        except ValueError:
            print("Por favor, ingrese una cantidad correcta.")

    while True: 
        try: 
            descuento = float(input("ingrese el porcentaje del descuento: "))
            if 0<= descuento <=100:
                break
            else:
                print("ingrese un valor valido.")
        except ValueError:
            print("por favor ingrese un descuento valido")

    # debemos de calcular el valor total

    subtotal =  precioUnitario*cantidad
    totalDesceunto = subtotal*(descuento/100)
    Valortotal = subtotal - totalDesceunto

    print("Resumen de la compra")
    print(f"producto: {producto}")
    print(f"precio unitario: ${precioUnitario:.2f}")
    print(f"cantidad: {cantidad}")
    print(f"descuento: {descuento}%")
    print(f"subtotal: ${subtotal:.2f}")
    print(f"descuento aplicado: ${totalDesceunto:.2f}")
    print(f"total a pagar: ${Valortotal:.2f}")

total()