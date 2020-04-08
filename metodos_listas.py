#metodos de listas

lista = ["Juan", "Luis", "Pedro"]
print(lista)

print("-----------")
#nos regresa el indice del elemento que queremos buscar en una lista, si es que existe
luis_index = lista.index("Luis") #1
print(luis_index)

print("-----------------")
#agregar un elemento al final de la lista
lista.append("Pablito")
print(lista)

print("------------------")
#agregar otra lista a la lista
lista_extra = ["Melo", "Topi", "Arturo"]
lista.extend(lista_extra)
print(lista)

print("------------------")
#agregar un dato a la lista
lista.insert(luis_index, "Luis")
print(lista)

#Regresa el numero de veces que hay un elemento
print(lista.count("Luis"))

print("---------------")
#elimiar el primer elemento de la lista que concuerde con el parametro recibido
lista.remove("Pablito")
print(lista)

print("---------------------------")
#elimina el ultimo elemento de la lista
elemento_quito = lista.pop()
#lista.pop()
print(lista)
print(elemento_quito)

print("---------------------")
#elimina el elemento del indice que digamos
lista.pop(luis_index)
print(lista)

print("------------------")
#invierte el orden de los elementos es una lista
lista.reverse()
print(lista)

print("---------------------")
#Ordenar una lista alfabeticamente: ASCENDENTO O DESCENDENTE
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

print("--------------------------")
#copia todo lo que tiene lista hasta el momento
copia = lista.copy()
print(copia)

print("--------------------")
#comprobamos que no se modifico la copia
lista.append("Yagel")
print(lista)
print(copia)

print("---------------------")
#elimina todos los elementos de una lista
lista.clear()
print(lista)