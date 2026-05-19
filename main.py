productos = [] # lista que tiene listas

def cargar_producto(lista):
    producto = []

    nombre = input("Ingresá el nombre del producto: ").lower()

    validar_codigo = False

    while validar_codigo == False:
        codigo = int(input("Ingresá el código: "))

        if len(lista) == 0:
            validar_codigo = True
        else:
            for i in range(len(lista)):
                if lista[i][0] == codigo:
                    print("Código repetido.")
                else:
                    validar_codigo = True

    if validar_codigo == True:
        producto.append(codigo)

    validar_precio = False

    while validar_precio == False:
        precio = int(input("Ingresá el precio: "))
        if precio <= 0:
            print("Precio inválido. Intente otra vez.")
        else:
            validar_precio = True

    validar_stock = False

    while validar_stock == False:
        stock = int(input("Ingresá el stock: "))
        if stock < 0:
            print("Stock inválido. Intente otra vez.")
        else:
            validar_stock = True

    producto += [nombre, precio, stock]
    lista.append(producto)

def mostrar_productos(lista):
    if len(lista) > 0:
        for i in range(len(lista)):
            print(f"Código: {lista[i][0]}")
            print(f"Nombre producto: {lista[i][1]}")
            print(f"Precio: {lista[i][2]}")
            print(f"Stock: {lista[i][3]}")
    else:
        print("No se cargaron productos para mostrar.")

def buscar_por_codigo(codigo, lista):
    for i in range(len(lista)):
        if codigo == lista[i][0]:
            print("Producto encontrado.")
            break
        else:
            print(f"{codigo}: producto no encontrado.")

# 5. Mostrar producto con menor stock
def mostrar_menor_stock(lista):
    producto_menor = lista[0][1]   # guardo el primer producto
    menor_stock = lista[0][3]      # guardo el primer stock 

    for i in range(len(lista)):
        if menor_stock < lista[i][3]:
            producto_menor = lista[0][1]
            menor_stock = lista[0][3]
        else:
            producto_menor = lista[i][1]
            menor_stock = lista[i][3]

    print(f"Producto: {producto_menor} -> Stock: {menor_stock}")

# 6. Calcular valor total del inventario
def calcular_inventario(lista):
    inventario = 0
    for i in range(len(lista)):
        inventario += lista[i][3] * lista[i][2]
    
    print(f"Inventario total: {inventario}")

"""
Menú
"""

menu = True

while menu == True:
    print("SUPERMERCADO PYTHON MARKET")
    opcion = int(input("Ingresá una opción: " \
    "\n\t1. Cargar producto." \
    "\n\t2. Mostrar productos." \
    "\n\t3. Buscar producto por código." \
    "\n\t4. Ordenar productos por precio." \
    "\n\t5. Mostrar producto con menor stock." \
    "\n\t6. Calcular valor total del inventario." \
    "\n\t7. Salir.\n\t"))

    match opcion:
        case 1:
            cargar_producto(productos)
        case 2:
            mostrar_productos(productos)
        case 3:
            codigo = int(input("Ingresá el código del producto a encontrar: "))
            buscar_por_codigo(codigo, productos)
        case 4:
            pass
            
        case 5:
            mostrar_menor_stock(productos)
        case 6:
            calcular_inventario(productos)
        case 7:
            print("Saliendo del sistema...")
            menu = False
        case _:
            print("Opción inválida. Intente nuevamente.")


