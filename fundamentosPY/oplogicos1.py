#Pide al usuario su edad y si tiene licencia de conducción. Solo si ambas condiciones se cumplen, imprime que puede conducir.

edad = int(input("ingresa tu edad: "))
lic= input("tienes licencia de conducción? (si/no:) ")

if edad >= 18 and lic == "si":
    print("felicidades puedes conducir")
else: 
    print("lo sentimos no puedes conducir")