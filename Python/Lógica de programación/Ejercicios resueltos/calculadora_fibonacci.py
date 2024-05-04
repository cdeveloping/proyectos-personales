#Solución calculadora Fibonacci

#Lo primero vamos a definir la secuencia de Fibonacci

def fibo(n):
    if  n <= 0:
        return "El indice debe ser un número entero"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[-1]

#Ahora comenzamos con los datos que necesitamos del usuario

while True:
    #Controlamos excepciones
    try:
        indice = (int(input("Introduce un número para calcular la secuencia, o introdue 0 para salir: ")))
        if indice == 0:
            print("Cerrando programa...")
            break
        resultado = fibo(indice)
        print(f"Elvalor en la secuencia de Fibonacci esta en el indice {indice}: {resultado}")
    except ValueError:
        print("El número que has introducido no es válido.")

