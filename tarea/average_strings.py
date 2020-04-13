words = [
    "jdjfjsdfjsdjf",
    "dsfsdf",
    "sssfdfsd"
]

print(sum( map(len,words)))
#map recorre una lista
total_avg = sum( map(len,words)) / len(words)
print(total_avg)