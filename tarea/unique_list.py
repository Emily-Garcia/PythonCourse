words = [
    "holi",
    "jajaja",
    "Holi",
    "holi",
    "emily",
    "diccionario",
    "emily"
]

#cn fromkeys asignas las llaves y las llaves no pueden ser repetidas
print(dict.fromkeys(words))

#Los diccionarios no puedes tener keys repetidas
new_list = list(dict.fromkeys(words))

print(words)
print(new_list)