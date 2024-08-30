


print("Hello world!") # imprimir en pantalla
numero = 7 # guardar dato tipo int en memoria, conocido como variable
palabra = "Python" # guardar dato tipo string en memoria, conocido como variable

print("---------- Esto es una suma ----------")
numero_dos = 2
numero_cuatro = 4
resultado = numero_dos + numero_cuatro
print(numero_dos, "+", numero_cuatro)
print("El resultado de la suma es = ", resultado)
resultado = str(resultado) # conversion de resultado numérico, a resultado string
print("El resultado de la suma es = " + resultado)

# asignamos más contenido a la variable sin borrar el valor anterior
print("---------- Asignación ----------")
mensaje = "Hola"
mensaje += " "
mensaje += "mundo"
print(mensaje)

# concatenación
print("---------- Concatenación ----------")
mensaje = "Hola"
espacio = " "
nombre = "Python"
print(mensaje + espacio + nombre)

# búsqueda
print("---------- Búsqueda ----------")
print("Hola Mundo")
mensaje = "Hola Mundo"
buscar_subcadena = mensaje.find("Mundo") # recordar que siempre empezamos a contar una posición en 0
print("La posición de la subcadena Mundo es: ", buscar_subcadena)

print("Hola Python")
mensaje = "Hola Python"
extraer_subcadena = mensaje[1:8]
print("Carácteres entre los límetes [1:8]: ", extraer_subcadena)

# comparación
print("---------- Comparación ----------")
print("Hola mundo")
mensaje_uno = "Hola mundo"
print("Hola Python")
mensaje_dos = "Hola Python"
print(mensaje_uno == mensaje_dos)

# exponente
print("---------- Exponente ----------")
print("2^5")
numero = 2
exponente = 5
resultado = numero ** exponente
print("El resultado de la exponente es: " + str(resultado))

# resto
print("---------- Resto ----------")
print("30/8")
numero_uno = 30
numero_dos = 8
resultado = numero_uno % numero_dos
print("El resultado del módulo es: " + str(resultado))

# división decimal
print("---------- División decimal ----------")
print("4/2")
numero_uno = 4
numero_dos = 2
resultado = numero_uno / numero_dos
print("El resultado de la división es: " + str(resultado))

# división entera
print("---------- División entera ----------")
print("10/3")
numero_uno = 10
numero_dos = 3
resultado = numero_uno // numero_dos
print("El resultado de la división es: " + str(resultado))

# tipo de dato entero o largo
print("---------- Tipo de dato ----------")
numero= 15
print(numero, type(numero))
# tipo de dato flotante
numero_flotante= 15.5
print(numero_flotante, type(numero_flotante))
# tipo de dato string
nombre= "Python"
print(nombre, type(nombre))

exit() # fin de proceso
