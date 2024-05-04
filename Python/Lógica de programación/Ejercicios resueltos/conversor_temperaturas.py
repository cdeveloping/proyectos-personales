#Ejercicio resuelto conversor de temperaturas

#Creamos unas funciones que hagan los calculos más adelante


#Función que hace la tranformación de celsius a Kelvin
def celsius_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

#Función que hace la conversión de Celsius a Farenheit
def celsius_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

#Creamos otra función para realizar los calculos con los datos del usuario
def conversion():
    celsius = float(input("Por favor introduzca la temperatura a convertir: " ))

    #Pasamos por parámetros los datos introducidos por el usuario a la función correspondiente
    grados_kelvin = celsius_kelvin(celsius)
    grados_farenheit = celsius_farenheit(celsius)

    print(f"{celsius} grados Celsius son: {grados_farenheit} grados Farenheit.")
    print(f"{celsius} grados Celsius son: {grados_kelvin} grados Kelvin.")


conversion()





