# Diccionario
productos = {
    "pera": 30,
    "pan": 15,
    "papa": 32,
    "manzana": 41
}

while True:
    print("\n-------------------------")
    print("---MENU---")
    print("\n1. Mostrar stock.")
    print("2. Agregar producto.")
    print("3. Quitar producto.")
    print("4. Salir.")

    opcion = int(input("\nElija una opción (1-4): "))
    print("\n-------------------------")

    # MOSTRAR STOCK
    if opcion == 1:
        print("---STOCK---\n")
        if not productos:
            print("\nEL INVENTARIO ESTA VACÍO.")
        else:
            for producto, cantidad in productos.items():
                print(f"Hay {cantidad} unidades de producto {producto} en stock.")

    # AGREGAR PRODUCTO
    elif opcion == 2:
        print("---AGREGAR PRODUCTOS---\n")
        producto = input("Ingrese el nombre del producto: ").lower()
        cantidad_agregar = int(input(f"Ingrese la cantidad de producto {producto} para agregar: "))
        if producto in productos:
            productos[producto] += cantidad_agregar
        else:
            productos[producto] = cantidad_agregar
        print(f"\nAgregaste {cantidad_agregar} unidades de producto {producto} en stock.")

    # QUITAR PRODUCTO
    elif opcion == 3:
        print("---QUITAR PRODUCTOS---\n")
        producto = input("Ingrese el nombre del producto: ").lower()
        cantidad_sacar = int(input(f"Ingrese la cantidad de producto {producto} para quitar: "))
        if producto in productos:
            if productos[producto] >= cantidad_sacar:
                productos[producto] -= cantidad_sacar
                print(f"\nQuitaste {cantidad_sacar} unidades de producto {producto} al stock.")
            else:
                print(f"\nNo hay suficiente stock de producto {producto}.")
        else:
            print(f"\nEl producto {producto} no se encuentra registrado en stock.")

    # SALIR
    elif opcion == 4:
        print("Saliendo...")
        break

    else:
        print("\n---OPCION INVÁLIDA---\nSELECCIONE UNA OPCIÓN DEL 1 AL 4.")