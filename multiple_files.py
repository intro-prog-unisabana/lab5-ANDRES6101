from utils import *

# pedir mensaje al usuario
mensaje = input("Please type your message\n")

# invertir el mensaje
mensaje_invertido = flip(mensaje)

# contar letras 'a'
cantidad_a = count_letters(mensaje, "a")

# crear mensaje codificado
mensaje_codificado = mensaje_invertido + str(cantidad_a)

# imprimir resultado
print(f"Your encoded message is: {mensaje_codificado}")