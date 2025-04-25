# Escribe una función que reciba un string y devuelva True si puede convertirse a número y False si no.

def es_numero(s):
    try:
        float(s) 
        return True
    except ValueError:
        return False

print(es_numero("123"))     
print(es_numero("12.34"))
print(es_numero("abc"))
print(es_numero("123abc"))
