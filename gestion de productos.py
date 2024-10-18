productos = []

def cargar_datos():
    """Carga los datos desde un archivo productos.txt."""
    try:
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': int(precio),
                    'cantidad': int(cantidad)
                })
    except FileNotFoundError:
        print("El archivo de productos no se encontró. Se iniciará con una lista vacía.")
    except Exception as e:
        print(f"Ocurrió un error al cargar los datos: {e}")

def guardar_datos():
    """Guarda los datos de productos en un archivo productos.txt."""
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")

def añadir_producto():
    """Añade un nuevo producto a la lista."""
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")

    try:
        precio = int(precio)
        cantidad = int(cantidad)
        producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        productos.append(producto)
        print(f"Producto '{nombre}' añadido con éxito.")
    except ValueError:
        print("Error: Precio y cantidad deben ser numéricos.")

def ver_productos():
    """Muestra todos los productos en la lista."""
    if not productos:
        print("No hay productos en la lista.")
    else:
        print("Lista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    """Actualiza los detalles de un producto existente."""
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            nuevo_nombre = input("Ingrese el nuevo nombre del producto (deje vacío para no cambiar): ")
            nuevo_precio = input("Ingrese el nuevo precio del producto (deje vacío para no cambiar): ")
            nuevo_cantidad = input("Ingrese la nueva cantidad del producto (deje vacío para no cambiar): ")

            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            if nuevo_precio:
                try:
                    producto['precio'] = int(nuevo_precio)
                except ValueError:
                    print("Error: El precio debe ser un número.")
            if nuevo_cantidad:
                try:
                    producto['cantidad'] = int(nuevo_cantidad)
                except ValueError:
                    print("Error: La cantidad debe ser un número.")
                
            print(f"Producto '{nombre}' actualizado con éxito.")
            return

    print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto():
    """Elimina un producto de la lista."""
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    global productos
    productos = [producto for producto in productos if producto['nombre'].lower() != nombre.lower()]
    print(f"Producto '{nombre}' eliminado." if any(producto['nombre'].lower() == nombre.lower() for producto in productos) else f"Producto '{nombre}' no encontrado.")

def menu():
    """Muestra el menú principal y maneja la selección del usuario."""
    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    cargar_datos()
    menu()
