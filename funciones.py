#creando una funcion 
def mi_funcion():
    print("hola comostas")

mi_funcion()

#Argumentos
#se definen despues del nombre de l funcion dentro del parentesis, y se pueden definir tantos como queramos, separados por comas

def imp_nombre(nombre, apellido):
    print("Hola,", nombre, apellido)

# imp_nombre("Arturo")
# imp_nombre("Melo")
# imp_nombre("Emily")

imp_nombre("Topi","Yagel")

#esto hara que se reciba una tupla de argumentos
def name(*kids):
    print("El niño mas peque es:" + kids[0])

name("Arturo","Melo","Topi")

def morritos(morrito1, morrito2, morrito3):
    print("El mas cool es", morrito2)

#si agregamos el parametro podemos definir un valor sin necesidad de pasar los argumentos en orden
morritos("Melo","Yo merengues","Tu sipsi")
#morritos( morrito2 = "Melo", morrito1 = "Yo merengues", morrito3 = "Tu sipsi")

#argumento por default
def pais(pais = "Tangamandapio"):
    print("Yo vivo en",pais)

pais()

#no es necesario definir el tipo de dato que va a recibir la funcion
def comida(comida):
    for comidita in comida:
        print(comidita)

comida("Maruchans")
    
print("---------------------")

#multiplicacion
def multiplicacion(x):
    #return regresa una variable
    return 5 * x

print(multiplicacion(5))

def pruebita():
    #pass no hace nada
    pass

pruebita()

#RECURSIVIDAD
#llamar una funcion dentro de si misma

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
print(factorial(4))

print("------------------------")

lista = ["Arturo","Melo","Topi"]

for elemento in lista:
    print(elemento)

#lo mismo pero con una funcion
print("--------------------------")

# def fooor(lista):
#     print(lista)
#     nlista=lista.pop(0)
#     fooor(lista)

# fooor(lista = ["Ya", "me", "salio", "jejeje"])
# # def fooor(lista):
# #     print(lista[0])

# # lista = ["Ya", "me", "salio", "jejeje"]

# # fooor()


