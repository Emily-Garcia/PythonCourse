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

    #Enumerate trae la longitud de la lista
    # trae el indice y el valor:
    #i es el contador
    # nota es la variable de la lista
    for i, nota in enumerate(notas):
        print(f"Calificacion #{i + 1}: {nota}")

    #sum hace la suma de una lista de numeros
    #len saca la longitud de una lista
    promedio = sum(notas)/len(notas)

    #operado ternario if else
    print(f'PROMEDIO: {promedio:.2f} - { "APROBADO" if promedio > 6 else "REPROBADO"}')