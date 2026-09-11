'''
Parte 1:
1. Crear una lista con los nombres de los y las clientes que
vamos a procesar. Recorrer la lista y mostrar el nombre de
cada cliente o clienta, junto con su posición en la lista (por
ejemplo, Cliente 1, Cliente 2, etc.).

2. Recorrer la lista con un for y mostrar el nombre de cada
cliente junto con su posición en la lista (por ejemplo: Cliente
1: Ana).

3. Si encuentras un nombre vacío, mostrar un mensaje de
alerta indicando que ese dato no es válido.

Ejemplo:

Cliente 1: Ana
Cliente 2: Juan
Cliente 3: [ALERTA] Nombre no válido
Cliente 4: Marta

Parte 2 (optativa)
Además, como bonus, probá aplicar el método .capitalize() de Python, que sirve para
poner en mayúscula la primera letra de una palabra y en minúscula el resto.

Ejemplo:

nombre = "mArIa"
print(nombre.capitalize())
'''

nombre = [ "  aNa ", "ERNesto ", " Claudio", " silvAna ", "", "  rocio", " HERnan", "MaNOlo", "Deborah", ""]

for i in range(len(nombre)):
    
    if nombre[i] == '':
        print(f"Cliente {i+1}: [ALERTA] nombre no valido")
    else:
        print(f"Cliente {i+1}: {nombre[i].strip().capitalize()}")
