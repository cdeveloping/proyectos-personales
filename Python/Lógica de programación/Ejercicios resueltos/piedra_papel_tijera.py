#Juego de Piedra, papel o tijera

#Importamos el método random() que usaremos más adelante
import random

#Creamos las opciones para el juego

opciones = ["piedra", "papel", "tijera"]

pc = random.choice(opciones) #El ordenador escojera una opción de manera aleatoria

usuario = input("Elige una opción (piedra, papel o tijera)").lower()

if usuario == pc:
    print("Has empatado")
elif (usuario == "piedra" and pc == "tijera") or \
    (usuario == "papel" and pc == "piedra") or \
    (usuario == "tijera" and pc == "papel"):
    print("Enhorabuena!!! Has ganado el juego")
else:
    print("Has perdido!!!! Más suerta la próxima vez")
    
       