#Aprobado o reprobado Crea un programa que reciba la calificación de un estudiante (0 a 100) e indique si está aprobado (60 o más) o reprobado (menos de 60).

nota = int(input("introduzca su calificación: "))
if nota >= 60:
    print("Felicidades!, aprobaste")
else:
    print("reprobado")

