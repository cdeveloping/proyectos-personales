#Morse Code Translate

codigo_morse = {
" " : "/",
"a" : ".-",
"b" : "-...",
"c" : "-.-.",
"d" : "-..",
"e" : ".",
"f" : "..-.",
"g" : "--.",
"h" : "...",
"i" : "..",
"j" : ".---",
"k" : "-.-",
"l" : ".-..",
"m" : "--",
"n" : "-.",
"o" : "---",
"p" : ".--.",
"q" : "--.-",
"r" : ".-.",
"s" : "...",
"t" : "-",
"u" : "..-",
"v" : "...-",
"w" : ".--",
"x" : "-..-",
"y" : "-.--",
"z" : "--.",
"0" : "-----",
"1" : ".----",
"2" : "..---",
"3" : "...--",
"4" : "....-",
"5" : ".....",
"6" : "-....",
"7" : "--...",
"8" : "---..",
"9" : "----."
}


#Pedimos al usuario el texto a traducir
mensaje = input("Por favor introduzca el mensaje a traducir: ")

#Como hemos creado el diccionario en minusculas transformamos todos los caracteres
minusculas = mensaje.lower()

#Creamos una variable para la traducción
traduccion = ""

for char in minusculas:
    traduccion += codigo_morse[char] + " "

print(traduccion)