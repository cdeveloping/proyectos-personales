#Ejercicio resuelto para contador de volales y consonantes


def contador_vocales_consonante(frase):
    contador_vocales = 0
    contador_consonantes = 0


    frase = frase.lower()

    for caracter in frase:
        if caracter in "aeiouáéíóúü":
            contador_vocales +=1
        elif caracter.isalpha():
            contador_consonantes +=1

    return contador_vocales, contador_consonantes


#Pedimos al usuario la frase

frase = input("Por favor introduce una pequeña frase: ")


vocales, consonantes = contador_vocales_consonante(frase)

print("La frase introducida contiene: ", vocales, " vocales.")
print("La frase introducida contiene: ", consonantes, " consonantes.")

