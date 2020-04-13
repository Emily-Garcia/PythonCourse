words = [
  'machine',
  'subset',
  'trouble',
  'starting',
  'matter',
  'eating',
  'truth',
  'disobedience'
]

input_word = input("Ingresa la palabra a buscar: ")

finded = False

for x in words:
  if x == input_word:
    print("ENCONTRAMOS LA PALABRA")
    print("La posicion es:", words.index(input_word))
    finded = True

if finded == False:
  print("Elemento no encontrado")
