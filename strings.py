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
splited = mensaje.split(" ")
print(splited)
splited = mensaje.split("a")
print(splited)