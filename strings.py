string = "Hola, mundo"

primer_letra = string[0]

#Checar la longitud de una cadena
longitud = len(string)

print("String: Hola, mundo")
print("Longitud:",longitud)

print("Primer letra:",primer_letra)

print("------------")

string = input("Escribe un mensaje: ")
primer_letra = string[0]
longitud = len(string)
#ultima_letra = string[len(string) - 1]
ultima_letra = string[-1]
print(ultima_letra)

print("---------")
#SLICES
mensaje = "Estoy aprendiendo a programar con Python"
#muestra todo lo que este apartir del indice que pongas entre[]
slicito_1 = mensaje[12:]
#muestra todo lo que esta antes del indice que pongas entre []
slicito_2 = mensaje[:21]
#muestra todo lo que esta entrre los rango que coloques en los []
slicito_3 = mensaje[6:17]

print(slicito_1)
print(slicito_2)
print(slicito_3)

print("-----------")
#Separar strings
splited = mensaje.split(" ")
print(splited)
splited = mensaje.split("a")
print(splited)
print(splited[1])

print("---------")
#LISTAS
lista = ["palabra", 3, 5.43, True, ["soy","otra","lista"]]
#meternos a uns lista anidada
print(lista[4][1])
#lista_anidada = lista[4]
#lista_anidada[1]

print("-------")
#Elemento quitado
nueva_lista = lista.pop()
#Quita el ultimo elemento de la lista
lista.pop()
print(lista)
print(nueva_lista)

print("------------")
#Agregar elemento al final
lista.append(False)
print(lista)

print("----------------")
#JOIN
#toma un lista de strings forzosamente y lo convierte a un solo string separado por el separador que le pongas
lista_string = ["1","2","3","4"]
separador = "-"

lista_joineada = separador.join(lista_string)
print(lista_joineada)