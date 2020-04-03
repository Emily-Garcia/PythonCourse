#El usuario ingrese el precio de su producto 
#se le muestre al final el valor del iva 

print("Vamos a calcular el valor del IVA")
valor_prod = float(input("Ingresa el valor del producto: "))

iva = valor_prod * 0.16

tot_prod = valor_prod + iva

print("El IVA del producto es:","{:0.2f}".format(iva))
print("El valor total del producto con IVA es:","{:0.2f}".format(tot_prod))