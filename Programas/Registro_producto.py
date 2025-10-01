def main():
    productos = []  # Lista para almacenar los productos
    
    # Recoger información sobre 3 productos
    for i in range(3):
        nombre = input(f"Ingrese el nombre del producto {i + 1}: ")
        precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
        producto = {"nombre": nombre, "precio": precio}  # Crear diccionario para el producto
        productos.append(producto)  # Agregar el producto a la lista

    # Calcular el total a pagar
    total = sum(producto["precio"] for producto in productos)

    # Mostrar la lista de productos y el total
    print("\nLista de Productos:")
    for producto in productos:
        print(f"Producto: {producto['nombre']}, Precio: ${producto['precio']:.2f}")
    
    print(f"\nTotal a pagar: ${total:.2f}")


if __name__ == "__main__":
    main()