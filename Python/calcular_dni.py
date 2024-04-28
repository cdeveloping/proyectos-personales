#Calculadora letra DNI  

def calculadora_dni(numero_dni):
    listado_letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    dni = int(numero_dni) % 23
    return listado_letras[dni]

numero_dni = input("Por favor introduce tu número de DNI sin la letra: ")
letra_dni = calculadora_dni(numero_dni)

print ("La letra del DNI es: ", letra_dni)
