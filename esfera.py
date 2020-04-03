import math

# 4/3 pi * r**3

print("Vamos a calcular el volumen de una esfera uwu")

radio = float(input("Ingresa el valor del radio de la esfera en cm: "))

#print("El valor de pi es de", math.pi)

#Se utilizan parentesis para que se realizen las operaciones dentro de ellas
volumen = (4/3 * math.pi) * (radio ** 3)

print("El volumen de tu esfera es de:","{:0.2f}".format(volumen),"cm3")
