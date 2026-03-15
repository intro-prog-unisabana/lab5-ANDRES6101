# Modifica la lista sumando un valor a cada elemento

def list_shift(valores, incremento):
    for i in range(len(valores)):
        valores[i] = valores[i] + incremento

# Calcula el promedio de una lista de floats.

def calc_avg(valores):
    if len(valores) == 0:
        return 0.0
    return float(sum(valores) / len(valores))

# Imprime una lista de floats

def print_normalized(valores):
    print(valores)


#uSO
datos = [2.0, 4.0, 6.0, 8.0]

prom = calc_avg(datos)
list_shift(datos, -prom)
print_normalized(datos)