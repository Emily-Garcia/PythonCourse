#FOR
# for(i=0,i<5,i++)

for i in range(5): #Empieza en el 0 y termina en el 5
    print("Hola usuario",i)

for i in range(1,10): #Empieza en 1 y termina en 10
    print("Hola usuario",i)

print("-----------------------")
#TABLAS DE MULTIPLICAR
for i in range(1,10):
    print(f"4 x {i} = {4*1}")
    # f" " - realizar operciones dentro de un string

print("-----------------------")

# for range ( variable del que se comienza, valor en que termina, va de 2 en 2)
print("Numeros pares hasta el 50")
for i in range(0, 52, 2):
    print(i)

print("-------------------------")
print("Lista de egresados")
personas = {"Arturo", "David", "Topi", "Martin"}

for persona in personas:
    print("Ing.", persona)

print("---------------------")
estudiantes = [
    ["Martin", [10, 10, 10]],
    ["Arturo", [7, 8, 9]],
    ["Chacha", [5, 10, 3]],
    ["Topa", [10, 8, 7]],
]

for estudiante in estudiantes:
    print("Nombre del alumno:", estudiante[0])
    print("Calificaciones:", estudiante[1])
 
print("---------------------")
estudiantes = [
    ["Martin", [10, 10, 10]],
    ["Arturo", [7, 8, 9]],
    ["Chacha", [5, 10, 3]],
    ["Topa", [10, 8, 7]],
]

for estudiante in estudiantes:
    print("Nombre del alumno:", estudiante[0])

    print("Calificaciones: ")

    notas = estudiante[1]

    calif_1 = notas[0]
    calif_2 = notas[1]
    calif_3 = notas[2]

    print(calif_1)
    print(calif_2)
    print(calif_3)

    prom = (calif_1 + calif_2 + calif_3)/3

    print(prom)

    if prom > 6:
        print("APROBADO")
    else:
        print("REPROBADO")