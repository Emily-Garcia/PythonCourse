#si x cosa es verdad haz esto, sino, haz lo otro

#no se usan llaves ni parentesis
condicion = False
#String vacio es Falsy, string con x cosa en Truthy
#None null False

#Truthy o Falsy
if condicion:
    print("Esto es verdadero")
else:
    print("Esto es falso")

calificacion = int(input("Ingrese su calificacion: "))

#Si
if calificacion >= 7:
    print("Ya pasaste")
#Te da otra opcion aparte de tu if y else
#Sino
elif calificacion >=5 and calificacion < 7:
    print("Si te rifas con un pomo, pasas")
#and or - operadores logicos
#and - validar que ambos valores sean Truthy => True
#or - validar que minimo uno de los valores sean Truthy => True
else:
    print("Ya ni vengas")
