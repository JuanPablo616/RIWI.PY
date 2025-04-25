#Solicita si una persona tiene experiencia laboral y título universitario. Usa operadores lógicos para decidir si puede aplicar a una oferta de trabajo.

experiencia = input("¿Tienes experiencia laboral? (si/no): ") 
titulo = input("¿Tienes titulo universitario? (si/no): ")

if experiencia == "si" and titulo == "si":
    print("felicidades, puedes aplicar a la oferta de trabajo")
else:
    print("lo sentimos, no puedes aplicar a la oferta de trabajo")