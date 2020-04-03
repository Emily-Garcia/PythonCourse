numero_1 = float(input("Agrega el primer valor"))
numero_2 = float(input("Agrega el segundo valor"))

total = numero_1 + numero_2

print("Total de la suma es:","{:0.2f}".format(total))

total = numero_1 * numero_2

print("Total de la multipicacion es:", "{:0.3f}".format(total))

total = numero_1 - numero_2

print("Total de la resta es:", "{:0.2}".format(total))

total = numero_1 ** numero_2

print("Total de la potencia es:", "{:0.2}".format(total))

total = numero_1 / numero_2

print("Total de la division es:", "{:0.2}".format(total))

total = numero_1 // numero_2

print("Total de la division exacta es:", total)

total = numero_1 % numero_2

print("El residuo de la division es:", "{:0.2}".format(total))
