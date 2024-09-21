lista_initiala = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

lista_initiala.sort()
lista_pare = lista_initiala[1::2]
print(lista_initiala)
lista_multipi_trei = []

for n in lista_initiala:
    if n % 3 == 0:
        lista_multipi_trei.append(n)

lista_initiala.reverse()
lista_impare = lista_initiala[1::2]
print(lista_initiala)

print(lista_pare)
print(lista_impare)
print(lista_multipi_trei)
