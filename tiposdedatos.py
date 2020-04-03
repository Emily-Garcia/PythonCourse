nombre = "Emily"

print("Hola, " + nombre)

#TIPOS DE DATOS
entero = 15
flotantes = 5.3423
string = "Texto"
booleano = True

# + - * ** / // %
#OPERADORES ARITMETICOS
suma = 4 + 5
resta = 5 - 4
multiplicacion = 5 * 4
potencia = 5 ** 2
division = 10 / 2
division_exacta = 5 // 2
modulo = 10 % 2

# print("El valor de tu suma es:", suma)

# + es para concatenar solo texto

#Para pedirle datos al usuario
print("Ingresa dos numeros a sumar")
numero_1 = float(input("Ingresa el primer valor: "))
numero_2 = float(input("Ingresa el segundo valor: "))

total = numero_1 + numero_2

print("Total de la suma es:","{:0.2f}".format(total))

print("Ingresa dos numeros a multiplicar")
numero_1 = float(input("Ingresa el primer valor: "))
numero_2 = float(input("Ingresa el segundo valor: "))

total = numero_1 * numero_2

print("Total de la multipicacion es:", "{:0.3f}".format(total))

print("Ingresa dos numeros a restar")
numero_1 = float(input("Ingresa el primer valor: "))
numero_2 = float(input("Ingresa el segundo valor: "))

total = numero_1 - numero_2

print("Total de la resta es:", "{:0.2}".format(total))

print("Ingresa dos numeros para calcular la potencia")
numero_1 = float(input("Ingresa el primer valor: "))
numero_2 = float(input("Ingresa el segundo valor: "))

total = numero_1 ** numero_2

print("Total de la potencia es:", "{:0.2}".format(total))

print("Ingresa dos numeros a dividir")
numero_1 = float(input("Ingresa el primer valor: "))
numero_2 = float(input("Ingresa el segundo valor: "))

total = numero_1 / numero_2

print("Total de la division es:", "{:0.2}".format(total))

print("Ingresa dos numeros a dividir (division exacta")
numero_1 = float(input("Ingresa el primer valor: "))
numero_2 = float(input("Ingresa el segundo valor: "))

total = numero_1 // numero_2

print("Total de la division exacta es:", total)

print("Ingresa dos numeros a dividir")
numero_1 = float(input("Ingresa el primer valor: "))
numero_2 = float(input("Ingresa el segundo valor: "))

total = numero_1 % numero_2

print("El residuo de la division es:", "{:0.2}".format(total))