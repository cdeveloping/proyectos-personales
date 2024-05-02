#Metodos de las cadenas en python

print("--- Uso de diferentes métodos en la cadenas ---")

print("*** Por favor selecciona una opción ***")
print("1. Upper().")
print("2. lower().")
print("3. Capitalize().")
print("4. count().")
print("5. Find().")
print("6. isdigit().")
print("7. isalum().")
print("8. isalpha().")
print("9. split().")
print("10. strip().")
print("11. replace().")
print("12. rfind().")

seleccion = input("Introduzca el número de opción: ")

while seleccion.isnumeric() == False:
    print("El valor debe ser númerico.")
    seleccion = input("Introduzca el número de opción: ")

    if (seleccion == 1):
        texto = input("Por favor introduzca el texto a convertir a mayúsculas: ")
        print(texto.upper())