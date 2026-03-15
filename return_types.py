def obtener_precio_usuario():
    precio = input("Enter the item's price:\n")
    return float(precio)


# USO
precio = obtener_precio_usuario()
print(precio)