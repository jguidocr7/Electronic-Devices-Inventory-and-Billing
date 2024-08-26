# Función de Login
def login():
    usuario = input("Ingrese el User ID: ")
    contrasena = input("Ingrese la contraseña: ")
    while usuario != "admin" or contrasena != "admin":
        print("El usuario o contraseña ingresados son incorrectos. Intente de nuevo.")
        usuario = input("Ingrese el User ID: ")
        contrasena = input("Ingrese la contraseña: ")
    print("Acceso concedido.")

# Función de menuPrincipal
def menuPrincipal():
    print("---- Menú Principal ----")
    print("1. Registrar nuevo stock de dispositivos")
    print("2. Consultar inventario")
    print("3. Facturación")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

# Función registroInventario para registrar dispositivos en el inventario
def registroInventario(dispositivosInventario, maxDispositivos):
    for i in range(maxDispositivos):
        if dispositivosInventario[i] == ["", 0, 0]:
            codigo = input(f"Especificar el código del dispositivo {i+1} a registrar: ")
            cantidad = int(input(f"Ingresar la cantidad del dispositivo {codigo}: "))
            precio = float(input(f"Ingresar el precio del dispositivo {codigo}: "))
            dispositivosInventario[i] = [codigo, cantidad, precio]
            print(f"Dispositivo {codigo} registrado correctamente.")
            
        else:
            print("No hay más espacio en el inventario para registrar nuevos dispositivos.")

# Función consultaInventario para imprimir todo el inventario
def consultaInventario(dispositivosInventario):
    print("---- Consulta de Inventario ----")
    for dispositivo in dispositivosInventario:
        if dispositivo[0] != "":
            print(f"Código: {dispositivo[0]}, Cantidad: {dispositivo[1]}, Precio Unitario: {dispositivo[2]} colones")

# Función de Facturación
def facturacion(dispositivosInventario):
    codigo = input("Especificar el código del dispositivo a facturar: ")
    cantidad = int(input(f"Especificar cuántas unidades del dispositivo {codigo} desea facturar: "))

    for dispositivo in dispositivosInventario:
        if dispositivo[0] == codigo:
            if dispositivo[1] >= cantidad:
                subprecio = dispositivo[2] * cantidad
                impuesto = subprecio * 0.13
                precioTotal = subprecio + impuesto
                dispositivo[1] -= cantidad
                print(f"Subtotal: {subprecio} colones")
                print(f"Impuesto (13%): {impuesto} colones")
                print(f"Precio total: {precioTotal} colones")
            else:
                print("No hay suficiente stock para realizar la facturación.")
            return
    print("El código ingresado no está registrado en el inventario.")



# Main
login()

maxDispositivos = int (input("Especificar cantidad de articulos que desea ingresar: "))  # Define la cantidad máxima de dispositivos que se podran registrar en el inventario
dispositivosInventario = [["", 0, 0] for _ in range(maxDispositivos)]  # declara el ARREGLO dispositivosInventario donde almacenamos los dispositivos a ingresar en inventario

# Ejecutar menú y funciones según la opción seleccionada

opcionMenu = True #variable para salir del while

while opcionMenu != False:
    opcion = menuPrincipal()
    if opcion == 1:
        registroInventario(dispositivosInventario, maxDispositivos)
    elif opcion == 2:
        consultaInventario(dispositivosInventario)
    elif opcion == 3:
        facturacion(dispositivosInventario)
    elif opcion == 4:
        print("Saliendo del sistema...")
        opcionMenu = False
    else:
        print("Opción inválida, intente nuevamente.")
