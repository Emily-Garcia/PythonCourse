#PRIMERO DEFINES LAS FUNCIONES

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def division_exacta(num1, num2):
    return num1 // num2

def elevar_cuadrado(num1):
    return num1 ** 2

#IMPRIMIR LOS RESULTADOS
def imprimir_res(nombre, valor):
    print(f'El resultado de la {nombre} es: {valor}')

def obt_num(num):
    return float(input(f'Dame el numero {num}: '))

# FUNCION PRINCIPAL
def main():
    num1 = obt_num(1)
    num2 = obt_num(2)
    # MANDAMOS LLAMAR LAS FUNCIONES
    sumaa = suma(num1,num2)
    restaa = resta(num1,num2)
    multi = multiplicacion(num1,num2)
    divi = division(num1,num2)
    divi_exacta = division_exacta(num1,num2)
    num1_cuad = elevar_cuadrado(num1)
    num2_cuad = elevar_cuadrado(num2)

    imprimir_res("suma",sumaa)
    imprimir_res("resta", restaa)
    imprimir_res("multiplicacion", multi)
    imprimir_res("division", divi)
    imprimir_res("division exacta", divi_exacta)
    imprimir_res("elevacion del numero uno al cuadrado",num1_cuad)
    imprimir_res("elevacion del numero dos al cuadrado",num2_cuad)

main()

#HACER QUELA CALCULADORA PUEDA ELEGIR N NUMEROS
#RECIBIR LOS NUMEROS CON UN SOLO INPUT, SEPARADOS POR COMAS
#ESCRIBE LOS NUMEROS A JUGAR CON ELLOS, SEPARADOS POR UNA COMA -> 5,6,5,5,6

# REALIZAR LA suma
# CALCULAR EL PRIMEDIO DE ODOS LOS NUMEROS
# CALCULAR LA multiplicacion DE TODOS LOS NUMEROS
# ELEVAR CADA UNO DE LOS NUMEROS AL elevar_cuadrado
# CALCULAR EL FACTORIAL DE CAD UNO DE LOS NUMEROS
