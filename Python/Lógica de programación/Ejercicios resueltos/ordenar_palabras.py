#Ordenar palabras alfabéticamente

print("*** Bienvenido a la aplicación para ordenar palabras ***")

texto = input("Por favor introduce tres palabras: ")
#Separamos las palabras
divisor = texto.split()

palabras_ordenadas = sorted(divisor)

print("Las palabras ordenadas alfabéticamente: ", palabras_ordenadas)