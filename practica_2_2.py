nombre = input("Ingrese su nombre: ") 
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
mail = input("Ingrese su mail: ")
if((nombre == "" or apellido == "" or mail == "") or edad < 18): #Verifica si alguno de los campos esta en blanco o edad es menor a 18
    print("ERROR\n")
else:  
    print("*"*11)
    print("* TARJETA *")
    print("*"*11)
    print("Nombre: ", nombre)
    print("Apellido: ", apellido)
    print("Edad: ", edad)
    print("Mail: ", mail)

