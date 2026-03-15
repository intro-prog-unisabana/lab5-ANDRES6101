def promedio_estudiante(calificaciones):

    if len(calificaciones) == 0:
        return 0.0
    
    promedio = sum(calificaciones) / len(calificaciones)
    return float(promedio)


# Llamar la función
notas = [50,10,3.6,40,2.5]
resultado = promedio_estudiante(notas)
print(resultado)