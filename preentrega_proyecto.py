'''
Pre-entrega de proyecto

Desarrollar un programa en Python que cumpla con las siguientes características:

Requerimientos:

* Ingreso de datos de productos:
El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría, y precio (sin centavos).
Estos datos deben almacenarse en una lista, donde cada producto sea representado/a como una sublista de
tres elementos (nombre, categoría, y precio).

* Visualización de productos registrados:
El programa debe incluir una funcionalidad para mostrar en pantalla todos los productos ingresados.
La información debe presentarse de manera ordenada y legible, con cada producto numerado.

* Búsqueda de productos:
El sistema debe permitir buscar productos por su nombre.
Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan.
Si no hay coincidencias, debe informar que no se encontraron resultados.

* Eliminación de productos:
El sistema debe permitir eliminar un producto de la lista, identificándolo por su posición (número) en la lista.

Requisitos

* Usar listas para almacenar y gestionar los datos.
* Incorporar bucles while y for según corresponda.
* Validar entradas del usuario o usuaria, asegurándote de que no se ingresen datos vacíos o incorrectos.
* Utilizar condicionales para gestionar las opciones del menú y las validaciones necesarias.
* Presentar un menú que permita elegir entre las funcionalidades disponibles: agregar productos, visualizar productos, buscar productos y eliminar productos.
* El programa debe continuar funcionando hasta que se elija una opción para salir.

Consejos

- Usá lo aprendido sobre listas y bucles para gestionar los datos y recorrerlos.
- Recordá validar las entradas utilizando condicionales.
- Utilizá las herramientas vistas para organizar y presentar la información de manera clara.

*** Ejemplo del menú de opciones: ***

Sistema de gestión básica de productos

1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir

'''

listado_productos=[]
producto = []
opcion = ""
nombre = ""
categoria= ""
precio = ""

while(opcion != "5"):

    #**** Imprime Menu ****
   
    tituloMenu = "Sistema de Gestion Basica de Productos"

    print(tituloMenu)
    print("*"*(len(tituloMenu)))

    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    print("\n" + "*"*(len(tituloMenu)))

    opcion = input("Ingrese una opcion del menu: ")

    #---- Ingreso de datos ----
    if (opcion == "1"):

        while(nombre == ""):
            nombre = input("Ingrese el nombre del producto: ").capitalize().strip()

            if(nombre == "" or not nombre.replace(" ", "").isalpha()):
                print("Error al ingresar el nombre, vuelva a ingresarlo.")
                nombre = ""

        while(categoria == ""):
            categoria = input("Ingrese la categoria del producto: ").capitalize().strip()

            if(categoria == "" or not categoria.isalpha()):
                print("Error al ingresar la categoria, vuelva a ingresarla.")
                categoria = ""

        while(precio == ""):
            precio = input("ingrese el precio del producto [El precio no puede incluir centavos]: $ ").strip()

            if(precio == "" or not precio.isdigit()):
                print("Error al ingresar el precio, vuelva a ingresarlo.")
                precio = ""
            elif(precio.isdigit()):
                precio = int(precio)

        listado_productos = listado_productos + [[nombre, categoria, precio]]
        nombre = ""
        categoria = ""
        precio = ""

    #---- Mostrar productos ----
    elif (opcion == "2"):

        if(len(listado_productos) == 0):
            print("No hay productos ingresados")
            continue
        
        print("*"*3 + "Listado de Productos" + "*"*3 + "\n")
        numero = 1
        for n in listado_productos:
            print(f"Nro. Prod: {numero} \t| Nombre: {n[0]} \t| Categoria: {n[1]} \t| Precio: $ {n[2]}")
            numero += 1

    #--- Buscar Producto ----                                                            
    elif (opcion == "3"):

        if listado_productos == []:
            print("No hay productos en la lista, no se puede realizar la busqueda.\n")
            continue

        encontrado = 0
        producto_buscado = input("Ingrese el producto a buscar: ").strip().lower()
       
        for x in listado_productos:
            if producto_buscado in x[0].lower():
                encontrado += 1
                print(f"Nombre: {x[0]} - Categoria: {x[1]} - Precio: $ {x[2]}")

        if encontrado == 0:
            print(f"\nEl Producto {producto_buscado} no se encontro en el listado.\n")
        else:
            print(f"Se encontraron {encontrado} producto/s.")

    #--- Eliminar producto ----
    elif (opcion == "4"):

        if listado_productos == [] :
            print("No hay elementos en la lista para eliminar.\n")
            continue
        
        eliminar = ""
       
        while eliminar == "":
            
            eliminar = input("Ingrese el numero del producto a eliminar: ")
            contador_eliminados = 0
            
            if (not eliminar.isdigit() or eliminar == ""):
                print("El valor ingresado no es un numero")
                eliminar = ""
                continue

            eliminar = int(eliminar)

            if (eliminar > len(listado_productos) or eliminar <= 0):
                print("El item seleccionado no esta en el listado de productos")
                eliminar = ""
                continue
        
            if (int(eliminar) <= int(len(listado_productos))):
                eliminar = eliminar - 1
                listado_productos.pop(eliminar)
                contador_eliminados += 1
                print(f"Se eliminaron {contador_eliminados} producto/s")

    #--- Salir del Programa ----        
    elif (opcion == "5"):
   
        print("Saliendo del sistema...")
        break

    else:

        print("Error en el ingreso de la opcion.\n")
        print("Ingrese una opcion valida entre 1 y 5.\n")

#Fin del programa
