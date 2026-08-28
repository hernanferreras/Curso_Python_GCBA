nombre = input("Ingrese el nombre: ").title()
apellido = input("Ingrese el apellido: ").title()
email = input("Ingrese el email: ").strip()
edad = int(input("Ingrese la edad: "))

if (edad < 15):
    rangoEtario = "Niño/a"
elif (edad <= 18 and edad >= 15):
    rangoEtario = "Adolescente"
else: 
    rangoEtario = "Adulto"

if(email.find("@") == -1):
    print("El email ingresado no es correcto, ingreselo nuevamente\n")
    email = input("Ingrese el email: ")

print(f"{nombre} {apellido} {email} {rangoEtario}")