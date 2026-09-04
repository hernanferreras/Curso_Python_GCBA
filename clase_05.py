cont_meses = 1
suma_ingreso = 0
while(cont_meses <= 6):

    ingreso = int(input(f"Ingrese el importe del mes {cont_meses}: "))

    if ingreso < 0:
        print("El importe no puede ser negativo, ingrese nuevamente")
    else:
        suma_ingreso += ingreso
        cont_meses += 1

print(f"El total de ingresos de los ultimos 6 meses es de ${suma_ingreso}")
    
