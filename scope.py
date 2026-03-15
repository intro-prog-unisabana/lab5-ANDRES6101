int_value = 0
str_value = 0

#Almacena un entero global y una cadena de texto global.

def set_globals(some_int, some_str):
    global int_value
    global str_value

    int_value = some_int
    str_value = some_str

#  valores guardados en las variables globales.

def get_globals():
    return (int_value, str_value)


#uso
print(get_globals())      
set_globals(10, "Hello")
print(get_globals())  