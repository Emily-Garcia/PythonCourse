# ¿Que es un diccionario?
# Estructura de datos (listas, diccionarios)
# Tenemos tipos diversos tipos de datos agrupados
# Listas, solo valores
# En los diccionaios tenemos pares de valres del tipo llave valor
# no importa si esta ordenado los datos

#diccionario
user = {
    #sintaxis
    #nombre de la llave = valor,
    "primer_nombre": "Emily",
    "apellido": "Garcia Quichimbo",
    "age": 19,
    "fecha_nac": "2000-11-11",
    # lista denro de un diccionario
    "comida_fav": ["Pizza", "tacos"],
    "direccion": {
        "calle": "sur 2",
        "manzana": 7,
        "lote": 25
    }
}

# son definidos usando llaves
# las llaves son del tipo string entonces deben ir entre "" (nombre de los atributos)

print(user)

#como traer un atributo especifico
print(user["primer_nombre"])

#que pasa si traigo una llave que no existe
#print(user["genero"])
#lanza un error

# como checar si una llave existe
print("genero" in user)
print("primer_nombre" in user)

#imprimir si existe la llave
if "genero" in user:
    print(user["genero"])
else:
    print("Llave Genero no existe")

if "apellido" in user:
    print(user["apellido"])
else:
    print("Lllave apellido no exite")

#checar si existe una llave, sino se pone un valor default
print(user.get("pais", "Mexico"))

#añadir nuevas llaves al diccionario
user["email"] = "garcia.16.emily@gmail.com"
print(user)

#actualizar una llave
print("UPDATEANDO")

user["email"] : "emikgq10@gmail.com"
print(user)

print("UPDATEANDO")
#eliminar una llave
del user["email"]
print(user)

print("----------------------")

perfil = {
    "foto_perfil" : "pikachu.jpg",
    "RFC" : "KSKDSKDKS",
    "hobbies" : "hacerme wey"
}

# juntar dos ususarios
user.update(perfil)
print(user)

#loop llaves y valores de un diccionario (recorrer)
for key, value in user.items():
    print("*****************")
    print("Llave:", key)
    print("Valor:", value)