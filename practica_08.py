'''
En TalentoLab nos han pedido desarrollar una aplicación que
registre productos y sus precios utilizando diccionarios.
Necesitamos que tu programa cumpla con estas
instrucciones:

* Crear un diccionario llamado productos donde las claves sean los nombres
de los productos y los valores sean sus precios.
* Permitir agregar productos y sus precios hasta que se decida finalizar.
* Mostrar el contenido del diccionario después de cada operación.
'''
listado = []
flag = False

while flag == False:

    nombre = input("Ingrese el nombre del producto ['fin' para terminar de ingresar]: ").capitalize()

    if nombre.lower() == "fin":

        print("*** Ingreso finalizado ***")
        flag = True
        break

    precio = input("Ingrese el precio del producto: ")

        
    if (nombre == "") or (precio == "") or ((int) precio <= 0):
        print("Error en el ingreso del producto y/o el precio. Vuelva a ingresarlos")
        continue

    else:

        producto = {
            "nombre": nombre,
            "precio": precio
        }
        listado.append(producto)
    
print("*"*3 + " Listado de Productos " + "*"*3 + "\n") 
for n in listado:
    print(f"Producto: {n['nombre']} -- Precio: ${n['precio']}")

print("\n" + "*"*28)
