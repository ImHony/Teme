
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

elem_comune = []

for i in a:
    if i in b:
        elem_comune.append(i)

print(elem_comune)
