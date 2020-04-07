#WHILE - MIENTRAS
print("===============================")
print("USANDO EL WHILE")

# Script to greet people. The program will stop when the user says S, if the option entered for the user is invalid, we have a nested while.
opt = 0
while opt != 'S':
  name = input("Por tu nombre pa saludarte, compa: ")
  print("Hola!", name)
  exit = input("Quieres salirte alv? (S/N): ")
  while exit != "S" and exit != "N":
    print("No mames, ingresa una opción válida")
    exit = input("Quieres salirte alv? (S/N): ")
  opt = exit
print("Gracias por dejame saludaaarte")

print('Vamos a la iglesia')
print('Me das tu diezmo?')

acum = 0
payments = 0

while payments < 10:
  pay = float(input('Ingresa tu diezmo a la iglesia: '))
  acum += pay
  payments += 1
print(f'Total de lo que le has pagado a la Iglesia: {acum:.2f}')