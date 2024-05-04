#Juego de adivina el número

#Generaremos un número aleatorio entre 1 y 100 y el usuario tiene 5 intentos

#Realizamos la importación de un metodo que necesitaremos para generar el número aleatorio
import random

def advina_el_numero():
    numero_a_adivinar = random.randint(1, 100)
    intentos_realizados = 0

    print("Tiene 5 intentos para intentar adivinar un número entre el 1 y el 100.")

    while intentos_realizados < 5:
        intento = int(input("Introduce tu intento: "))


        if intento != numero_a_adivinar:
            print("El número introducido no es correcto")
        else:
            print(f"Enhorabuna el número introducido es correcto, el numero era: {numero_a_adivinar}")

        intento_restantes = 4 - intentos_realizados
        if intento_restantes > 0:
            print(f"Te quedan {intento_restantes} intentos.")
        else:
            print(f"Lo siento, has  agotado los intentos, el número secreto era: {numero_a_adivinar}")
            return
        
        intentos_realizados +=1

advina_el_numero()


