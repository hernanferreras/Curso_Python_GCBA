'''
¡Hola!
Tu tarea es crear un programa en Python con las siguientes características:
● Agregar productos: Permite a la usuaria/o agregar productos a una lista. Cada producto debe
tener un nombre y un precio.
● Consultar productos: Muestra todos los productos en la lista junto con sus precios.
● Eliminar productos: Elimina un producto de la lista a partir de su nombre.
● Menú interactivo: El programa debe ofrecer un menú para que el usuario o usuaria pueda elegir qué acción realizar. 
Debe incluirse una opción para salir del programa.
'''

productos = []

#Funcion para agregar productos
def agregar_productos(productos):
    #nombre = input("Ingrese el producto: ").strip().capitalize()
    nombre_producto = ingresar_nombre_producto()
    precio = ingresar_precio()
    producto = [nombre_producto, precio]
    productos.append(producto)
    print(f"El producto {producto[0]} fue agregado existosamente")

#Funcion para consultar productos
def consultar_productos():
    
    global productos
    
    if len(productos) == 0:
        print("La lista de productos esta vacia")
    else:

        i = 1
        print("*** Listado de Productos ***")
        for x in productos:
            print(f"Nro Producto: {i}\t | Nombre: {x[0]}\t | Precio: ${x[1]}")
            i += 1
        print("****************************\n")

#Funcion para eliminar productos
def eliminar_productos(productos):

    producto_eliminado = input("Ingrese el nombre del producto a eliminar: ").strip().lower()
    eliminado = False 

    for x in productos:
        
        producto_buscado = x[0].lower()
    
        if producto_buscado == producto_eliminado:
            productos.remove(x)
            print(f"Producto \"{producto_buscado.capitalize()}\" eliminado correctamente de la lista")
            eliminado = True

    if (eliminado == False):    
        print(f"No existe el producto {producto_eliminado.capitalize()} en la lista de productos")
    

#Funcion para ingresar el nombre del producto
def ingresar_nombre_producto():

    nombre = ""

    while(nombre == ""):
        
        nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
        
        if(not isinstance(nombre, str)):
            print("El nombre ingresado es incorrecto, vuelva a ingresarlo")
            nombre = ""
            continue
        else: 
            return nombre

#Funcion para ingresar precio
def ingresar_precio():
    
    precio = ""
    
    while(precio == ""):
        precio = input("Ingrese el precio del producto: ").strip()
        if (precio.isdigit() == False or precio == "0"):
            print("El precio ingresado es incorrecto, vuelva a ingresarlo")
            precio = ""
            continue
        else:
            return int(precio)
 
###### MAIN ######

opcion = ""

while (opcion != "4"):

    #Muestra Menu
    print("*"*5 + "Listado de Productos" + "*"*5)
    print("Opcion - Detalle\n")
    print("1 - Agregar Producto")
    print("2 - Consultar Producto")
    print("3 - Eliminar Producto")
    print("4 - Salir del Programa")
    print("*"*5 + "*"*len("Listado de Productos") + "*"*5)

    #Selecciona Opcion
    opcion = input("Eliga una opcion del menu: ")

    if(opcion == "1"):
        agregar_productos(productos)

    elif(opcion == "2"):
        consultar_productos()

    elif(opcion == "3"):
        eliminar_productos(productos)

    elif(opcion == "4"):
        continue

    else:
        print("La opcion elegida es erronea, vuelva a ingresarla")

print("Saliendo del programa...")
