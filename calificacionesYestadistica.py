#Desarrollar un programa en Python que gestione una serie de calificaciones y estadísticas de manera interactiva
#Determinar el estado de aprobación
calificaciones = []

while True:
    try:
        entrada = input("Ingrese su calificación obtenida de 0-100, separada por coma (para finalizar ingrese 'salir'): ").strip()
        
        if entrada.lower() == "salir":
            break
        
        lista_nota = [int(x.strip()) for x in entrada.split(",")]
        print("Estas son tus calificaciones obtenidas:", lista_nota)
        
        for nota in lista_nota:
            if 0 <= nota <= 100:
                if nota >= 60:
                    print(f"Calificación {nota}: Felicidades ¡Aprobaste!")
                else:
                    print(f"Calificación {nota}: Lo sentimos, reprobaste.")
                calificaciones.append(nota)
            else:
                print(f"Calificación {nota} fuera de rango. Debe estar entre 0 y 100.")
    except ValueError:
        print("Por favor, ingresa una calificación válida.")
        
print(f"estas son tus calificaciones obtenidas, {calificaciones}")

#Calcular el promedio de las calificaciones
if calificaciones:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"El promedio de sus calificaciones es: {promedio: .2f}")

#Solicitamos al usuario que ingrese un numero entre (0-100)

    num1 = int(input("ingrese un número entre (0-100):"))

#mostrarmos cuántas calificaciones en la lista son mayores que ese valor.

    mayores = [nota for nota in calificaciones if nota > num1]
    print(f"Las calificaciones mayores a {num1} son: {mayores}")

#solicitamos el ingreso de una calificacion para contar cuantas veces aparece en la lista

if calificaciones:
    calificacion_especifica = int(input("Ingrese una calificación específica para contar cuántas veces aparece: "))
    contador = calificaciones.count(calificacion_especifica)
    print(f"La calificación {calificacion_especifica} aparece {contador} veces en la lista.")
else:
    print("No se ingresaron calificaciones válidas.")