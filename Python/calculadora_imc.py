#Aplicación con la que podrás calcular tu IMC (Indice de masa corporal)

peso = float(input("Por favor introduzca su peso en Kg: "))
altura = float(input("Por favor introduzca su alutar en metros: "))
altura_formula = altura ** 2 

imc = peso / altura_formula

print("Su IMC actual es: ", imc)

if imc < 18.5:
    print("Su peso es demasiado bajo.")
elif imc < 24.9:
    print("Su peso está dentro de los valores normales.")
elif imc < 29.9:
    print("Atención está en pre-obesidad o Sobrepeso")
elif imc < 34.9:
    print("Atención!! Obesidad Clase 1, pongase en contacto con un especialista urgentemente.")
elif imc < 39.9:
    print("Atención!! Obesidad Clase 2, pongase en contacto con un especialista urgentemente.")
elif imc >= 40:
    print("Atención!! Obvesidad Clase 3, pongase en contacto con un especialista urgentemente.")
else:
    ("Los datos no pueden ser analizados.")
