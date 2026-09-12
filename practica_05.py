'''
Para este ejercicio necesitamos un software que ayude a registrar y calcular información financiera básica para nuestros clientes.
Tu tarea para esta semana es la siguiente:

1 - Registrar los ingresos mensuales de un cliente durante 6 meses usando un bucle while para solicitar el ingreso de cada mes. 
Validar que los ingresos sean números positivos. 
Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.

2 - Calcular el total acumulado durante los 6 meses y el promedio mensual.
Mostrá este resultado al final del programa.
'''
totalAcumulado = 0;
mes = 1

while(mes <= 6):
    ingresoMensual = int(input(f"Ingrese el sueldo del mes {mes}: "))

    if(ingresoMensual < 0):
        print("El valor ingresado es invalido, vuelva a ingresarlo")
    else:
        totalAcumulado += ingresoMensual
        mes += 1

print("El total acumulado de los ultimos 6 meses es de : ", totalAcumulado)