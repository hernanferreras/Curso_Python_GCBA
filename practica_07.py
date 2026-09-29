'''
En TalentoLab necesitamos llevar un registro ordenado de los  nombres de los nuevos clientes
y clientas que se van incorporando.
Queremos asegurarnos de que los datos ingresados sean válidos y estén bien organizados. 
Tu tarea es escribir un programa en Python que haga lo siguiente:

1. Solicite al usuario o usuaria los nombres de los clientes y clientas uno por uno y
valide que cada nombre no esté vacío. Si se deja el campo vacío, mostrale un
mensaje de advertencia y volvé a pedir el nombre.
2. Guarde cada nombre válido en una lista, asegurándote de agregarlo con el
método .append().
3. Permita que la persona finalice la carga de nombres escribiendo la palabra "fin".
4. Una vez finalizada la carga, ordene alfabéticamente los nombres en la lista y
muestre la lista ordenada de nombres utilizando un bucle for.

'''

lista_nombres = []

flag = False

while(flag != True):

    nombre = input("Ingrese el nombre del cliente/a: ")

    if nombre == "":

        print("Error en el ingreso del nombre\nIngreselo nuevamente")
        
    elif (nombre != "fin"):

        lista_nombres.append(nombre)

    else:

        flag = False
        break

lista_nombres.sort()
contador = 1

print("\nListado de Clientes por Orden Alfabetico:\n")
for n in lista_nombres:

    print(f"Nombre del cliente {contador} : {n} ")
    contador += 1

    