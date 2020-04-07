#para sacar numeros randoms
from random import randint

jugador = int(input("Que arma escoges? (1)Piedra (2)Papel (3)Tijera: "))

computadora = randint(1,3)

if jugador == 1:
    jug = "Piedra"
elif jugador == 2:
    jug = "Papel"
elif jugador ==3:
    jug = "Tijeras"

if computadora == 1:
    com = "Piedra"
elif computadora == 2:
    com = "Papel"
elif computadora == 3:
    com = "Tijeras"


print("JUGADOR:",jug)
print("COMPUTADORA:",com)

if jugador == 1 and computadora == 1:
    print("---EMPATE!")
elif jugador == 1 and computadora == 2:
    print("---PERDISTE!")
elif jugador == 1 and computadora == 3:
    print("---GANASTE!")
elif jugador == 2 and computadora == 1:
    print("---GANASTE!")
elif jugador == 2 and computadora == 2:
    print("---EMPATE!")
elif jugador == 2 and computadora == 3:
    print("---PERDISTE!")
elif jugador == 3 and computadora == 1:
    print("---PERDISTE!")
elif jugador == 3 and computadora == 2:
    print("---GANASTE!")
elif jugador == 3 and computadora == 3:
    print("---EMPATE!")
