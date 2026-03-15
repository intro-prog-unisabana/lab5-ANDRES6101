def promedio_estudiante(calificaciones):

    if len(calificaciones) == 0:
        return 0.0
    
    suma = sum(calificaciones)
    cantidad = len(calificaciones)
    
    promedio = suma / cantidad
    
    return float(promedio)