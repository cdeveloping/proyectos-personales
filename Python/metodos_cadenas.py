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

while (seleccion.isdigit() == False):
    print("El valor debe ser númerico.")
   
    seleccion = input("Introduzca el número de opción: ")
#Pasamos todo a mayusculas
if (int(seleccion) == 1):
     texto = input("Por favor introduzca el texto a convertir a mayúsculas: ")
     print(texto.upper())
#Pasamos todo a minusculas
elif(int(seleccion) == 2):
    texto = input("Introduce el texto a transformar a minusculas: ")
    print(texto.lower())
#Ponemos la primera letra en mayúscula
elif(int(seleccion) == 3):
    texto = input("Introduce una palabra con la primera letra en minuscula: ")
    print(texto.capitalize())
#Contamos un caracter
elif(int(seleccion) == 4):
    texto = input("Introduce un pequeño texto: ")
    caracter = input("Introduce el caracter que quieres buscar en tu texto: ")
    conteo = texto.count(caracter)
    print("El caracter ", caracter, " aparece ", conteo, " veces en el texto que has introducido.")
#Buscar primera coincidencia en una cadena
elif(int(seleccion) == 5):
    texto = input("Introduzca un pequeño texto: ")
    palabra = input("Introduzca la palabra a buscar en el texto: ")
    buscar = texto.find(palabra)
    if(buscar <= 0):
        print("Lo siento la palabra no se encuentra dentro del texto")
    else:
        print("La plabra ", palabra, " se encuentra en la posición: ", buscar)
#Comprobamos si el valor introducido es numerico        
elif(int(seleccion) == 6):
    numero = input("Introduzca un valor numerico: ")
    comprobación = numero.isnumeric()
    if(comprobación == True):
        print("El dato introducido es correcto.")
    else:
        print("El valor introducido no es correcto.")
#Comrpobamos si los valores introducidos son alfanumericos
elif(int(seleccion) == 7):
    texto = input("Introduce un pequeño texto para comprobar: ")
    comprobación = texto.isalnum()
    if(comprobación == True):
        print("El texto introducido es alfanumerico")
    else:
        print("El texto introducido no es alfanumerico")
#Comprobación si es una cadena alfabetica unicamente
elif(int(seleccion) == 8):
    texto = input("Introduzca un pequeño texto: ")
    comprobación = texto.isalpha()
    if(comprobación == True):
        print("El texto introducido es alfabetico exclusivamente, o contiene espacios entre texto y números.")
    else:
        print("El texto introducido no es alfabetico unicamente.")
#Dividir una cadena en subcadenas
elif(int(seleccion) == 9):
    texto = input("Por favor escriba un pequeño texto: ")
    divisor = texto.split()
    print(divisor)
#Eliinar espacios en blanco al principio y al final de la cadena
elif(int(seleccion) == 10):
    texto = input("Por favor escriba un pequeño texto para comprobar: ")
    borrador = texto.strip()
    print(borrador)
#Reemplazar una palabra
elif(int(seleccion)== 11):
    texto = input("Por favor introduzca un pequeño texto: ")
    print("El texto introducido es: ", texto)
    reemplazo = input("Introduzca la palabra que quiere reemplazar: ")
    reemplazo2 = input("¿Por qué palabra la quiere reemplazar?: ")
    text2 = texto.replace(reemplazo, reemplazo2)
    print(text2)
#Buscar una subcadena dentro de una cadena
elif(int(seleccion) == 12):
    texto = input("Por favor introduzca un pequeño texto de prueba: ")
    busqueda = input("¿Qué palabra quiere buscar?: ")

    resultado = texto.rfind(busqueda)
    print(resultado)


else:
    print("Opción no autorizada")