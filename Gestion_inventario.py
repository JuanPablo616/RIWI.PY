#Desarrollar un programa en Python que permita gestionar de manera eficiente el inventario de productos de una tienda, aplicando funciones con parámetros, funciones lambda, y estructuras de datos como listas, tuplas y diccionarios.

inventario = []
def agregar_produc(inventario, nombre, precio, cantidad):
    if nombre in inventario:
        print(f"Error: el producto {nombre} ya existe en el inventario.")
    else:
        inventario[nombre] = (precio, cantidad)
        print(f"el producto {nombre} ha sido añadido correctamente.")
        
def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\nInventario actual: ")
        for nombre, (precio, cantidad) in inventario.items():
            print(f"{nombre}- $ {precio:.2f}- Cantidad: {cantidad}")
            
def actualizar_produc(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    if nombre not in inventario:
        print(f"Error: el producto {nombre} no se encuentra en el inventario.")
    else:
        precio, cantidad = inventario[nombre]
        if nuevo_precio is not None:
            precio = nuevo_precio
        if nueva_cantidad is not None:
            cantidad = nueva_cantidad
        inventario[nombre] = (precio, cantidad)
        print(f"nuevo producto {nombre} ingresado.")
        
def elim_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"{nombre} ha sido eliminado del inventario.")
    else:
        print(f"El producto {nombre} no se encuentra en el inventario.")
        
from functools import reduce
def calcular_invent(inventario):
    total = reduce(
        lambda acumulado, item: acumulado + item[1][0]* item[1][1],
        inventario.items(),0)
    print(f"\nValor total del inventario: ${total:.2f}")
    
def menu():
    inventario={}
    
    while True:
        print("\nMenú de gestión de Inventario:")
        print("1. Añadir producto")
        print("2. Mostrar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario.")
        print("6. Salir")
        
        opcion = input("ingrese una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio del producto: "))
                cantidad = int(input("Cantidad disponible: "))
                agregar_produc(inventario, nombre, precio, cantidad)
            except ValueError:
                print("Error: ingrese un valor valido para su producto.")
                
        elif opcion =='2':
            mostrar_inventario(inventario)
        
        elif opcion =='3':
            nombre = input("Nombre del producto por actualizar: ")
            try:
                nuevo_precio = input("nuevo precio: (sino va cambiar el precio presione enter.)")
                nueva_cantidad = input("Nueva cantidad: (sino va cambiar la cantidad presione enter. )")
                
                nuevo_precio= float(nuevo_precio) if nuevo_precio else None
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                
                actualizar_produc(inventario, nombre, nuevo_precio, nueva_cantidad)
            except ValueError:
                print("Error: digite un valor valido para su producto")
                
        elif opcion == '4':
            nombre = input("Digite el nombre del producto que desea eliminar: ")
            elim_producto(inventario,nombre)
            
        elif opcion =='5':
            calcular_invent(inventario)
            
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        
        else: 
            print("Opción no valida. por favor digite nuevamente.")
            
if __name__ == "__main__":
    menu()