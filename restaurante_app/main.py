from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n" + "=" * 40)
    print("      SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 40)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 40)
    print("6. Salir")

def registrar_producto(restaurante: Restaurante):
    print("\n---Registrar Producto---")
    nombre = input("Nombre del producto: ").strip()
    codigo = input("Código del producto: ").strip()
    categoria = input("Categoría del producto: ").strip()

    try:
        precio = float(input("Precio del producto: "))
    except ValueError:
        print("Error: El precio debe ser un número válido.")
        return
   
    producto = Producto(nombre, codigo, precio, categoria)
    registrado = restaurante.registrar_producto(producto)

    if registrado:
        print("Producto registrado correctamente.")
    else:
        print("Ya existe un producto con ese código.")

def registrar_bebida(restaurante: Restaurante):
    print("\n--- Registrar Bebida ---")
    nombre = input("Nombre de la bebida: ").strip()
    codigo = input("Código de la bebida: ").strip()
    tamano = input("Tamano de la bebida: ").strip()

    try:
        precio = float(input("Precio de la bebida: "))
    except ValueError:
        print("Error: El precio debe ser un número válido.")
        return

    bebida = Bebida(nombre, codigo, precio, tamano)

    if restaurante.registrar_producto(bebida):
        print("Bebida registrada correctamente.")
    else:
        print("Ya existe un producto con ese código.")

def registrar_cliente(restaurante: Restaurante):
    print("\n--- Registrar Cliente ---")
    nombre = input("Nombre del cliente: ").strip()
    email = input("Email del cliente: ").strip()
    identificacion = input("Identificación del cliente: ").strip()

    cliente = Cliente(nombre, email, identificacion)

    if restaurante.registrar_cliente(cliente):
        print("Cliente registrado correctamente.")
    else:
        print("Ya existe un cliente con esa identificación.")

def main ():
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        
        elif opcion == "2":
            registrar_bebida(restaurante)
        
        elif opcion == "3":
            registrar_cliente(restaurante)

        elif opcion == "4":
            print("\n--- LISTA DE PRODUCTOS Y BEBIDAS ---")
            restaurante.listar_productos()

        elif opcion == "5":
            print("\n--- LISTA DE CLIENTES ---")
            restaurante.listar_clientes()
        
        elif opcion == "6":
            print("\nSesión finalizada. ¡Buen día!")
            break
        else:
            print("Lo siento, esa opción no está disponible. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

