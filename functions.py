def promedio_estudiante(calificaciones):
    if len(calificaciones) == 0:
        return 0.0
    
    promedio = sum(calificaciones) / len(calificaciones)
    return float(promedio)


#USO
notas = [85, 92, 78]
print(promedio_estudiante(notas))

