words = [
  'machine',
  'matter',
  'subset',
  'trouble',
  'starting',
  'matter',
  'eating',
  'matter',
  'truth',
  'disobedience',
  'matter',
  'truth'
]

count = 0
found = False

input_word = input("Que palabara quieres buscar? ")

for x in words:
  if x == input_word:
    count += 1
    found = True

print("Palabra:", input_word, "- Veces que se repite:", count)