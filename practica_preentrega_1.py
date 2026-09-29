lista_precios = {'manzana': 150, "banana": 200, "pera": 230}
print(lista_precios['manzana'])
#print(lista_precios.values())
cambio_manzanas = int(input("Ingrese el nuevo precio del item manzana: "))
lista_precios['manzana'] = cambio_manzanas
print(lista_precios['manzana'])

print("*** Precio de Frutas ***")
for producto, precios in lista_precios:
    print(f"{lista_precios[producto]} : $ {lista_precios[precios]}")
