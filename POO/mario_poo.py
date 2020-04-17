import random

class MarioBros:
    personajes = ['normal', 'grande', 'fuego']
    def __init__(self, vidas, monedas, personaje):
        self.vidas = vidas
        self.monedas = monedas
        self.personaje = personajes[personaje-1]

    def get_actual_status(self):
        print('No. de vidas:', self.vidas)
        print('No. de monedas:', self.monedas)
        print('Personaje actual:', self.personaje)

    def killed(self):
        self.vidas -= 1
        self.personaje = self.personajes[0]
        print('Amá, me morí')
        if self.vidas == 0:
            print('Gracias por jugar, F')

    def eat_green_mushroom(self):
        self.vidas += 1
        print('Tengo una oportunidad más pa morirme')

    def get_coin(self):
        self.monedas += 1
        print("+1 moneda")
        if self.monedas == 100:
            self.eat_green_mushroom()
            monedas = 0

    def eat_red_mushroom(self):
        print("Estupefacientes color rojo")
        if self.personaje == self.personajes[0]:
            self.personaje = self.personajes[1]

    def eat_flower(self):
        print("Florecita para el estomágo")
        if self.personaje == self.personajes[0]:
            self.personaje = self.personajes[1]
        elif self.personaje == self.personajes[1]:
            self.personaje = self.personajes[2]

    def attacked_by_something(self):
        print("Amá, me pegaron")
        if self.personaje == self.personajes[2]:
            self.personaje = self.personajes[1]
        elif self.personaje == self.personajes[1]:
            self.personaje = self.personajes[0]
        elif self.personaje == self.personajes[0]:
            self.killed()

    def fall(self):
        print('Amá, me caí')
        self.killed()

def main():
    opc = 'S'
    vidas = int(input('Ingresa el número de vidas actual: '))
    monedas = int(input('Ingresa el número de monedas actual: '))
    print('1.- Normal')
    print('2.- Grande')
    print('3.- Fuego')
    personaje = int(input('Ingresa el personaje de Mario actual: '))
    mario_bros = MarioBros(vidas, monedas, personaje)

    while (opc != 'N'):
        random_option = random.randint(1, 7)
        if random_option == 1:
            mario_bros.eat_red_mushroom()
        elif random_option == 2:
            mario_bros.eat_green_mushroom()
        elif random_option == 3:
            mario_bros.get_coin()
        elif random_option == 4:
            mario_bros.eat_flower()
        elif random_option == 5:
            mario_bros.attacked_by_something()
        elif random_option == 6:
            mario_bros.fall()
        else:
            mario_bros.killed()

        mario_bros.get_actual_status()
        print("------------------------")
        opc = input('¿Deseas seguir jugando con Mario? (S/N): ')

    print('De nada vuelva pronto')

main()