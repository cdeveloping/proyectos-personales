#Solución al ejercicio de contar las palabras que componen un texto

print("*** Bienvenido al contador de palabras ***")

#Pedimos al usuario la frase
frase = input("Por favor introduce una pequeña frase: ")

#Dividimos la frase en palabras usando el método split() y con el método len las contamos
divisor = len(frase.split())

#Mostramos el número por consola
print("La frase introducida tiene ", divisor, " palabras.")

