datos = {
    "nombre" : input("Ingresa tu nombre: "),
    "apellidos" : input("Ingresa tu apelllido: "),
    "edad" : input("Ingresa tu edad: "),
    "email" : input("Ingresa tu email: ")
}

for key, value in datos.items():
    print(key,": ",value)

