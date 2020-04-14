#PIDE LOS NUMEROS

print("Ejm: 2,3,5,4,3,6")
num = input("Escribe los numeros a jugar con ellos, separados por una coma: ")

print(num)

#QUITAR LAS COMAS

numeros = num.split(",")
print(numeros)

#NUM DE DIGITOS

longitudnum = len(numeros)
print(longitudnum)

print("----------------------------")
for n in numeros:
    print(n)

#SUMA 
print("---------------------------------------------------")
suma = 0

for n in numeros:
    suma = suma + int(n)

print(suma)

#PROMEDIO
print("---------------------------------------------------")

promedio = suma/longitudnum
print(promedio)

#MULTIPLICACION
print("---------------------------------------------------")
mult = 1

for n in numeros:
    mult = mult * int(n)

print(mult)

#AL CUADRADO
print("---------------------------------------------------")

for n in numeros:
    cuad = int(n) ** 2
    print(cuad)

#FACTORIAL
print("---------------------------------------------------")

for n in numeros:
    tope=int(n)
    fact = int(n)
    for i in range(1,tope):
        fact = fact * i
    print(fact)
    print("---")

