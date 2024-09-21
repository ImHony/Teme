# CNP VALID: 5020430430041
# CNP INVALID: 6011230456789

# Constante
LISTA_CONTROL = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

cnp = input("Te rog tasteaza CNP-ul pentru validare: ")

# Validare string
cnp_valid = None
for caracter in cnp:
    if (caracter.isalpha() or caracter.isalnum) and len(cnp) != 13:
        cnp_valid = 0

if cnp_valid == 0:
    print("CNP-ul introdus NU respecta formatul corect")


lista_cnp_de_analizat = []
for i in cnp:
    lista_cnp_de_analizat.append(int(i))

print(f"CNP-ul de analizat este: {lista_cnp_de_analizat}")
print(f"Lista de control este: {LISTA_CONTROL}")
lista_elemente_inmultite = []
for i in range(12):
    lista_elemente_inmultite.append(LISTA_CONTROL[i] * lista_cnp_de_analizat[i])

print(f"Lista elementelor inmultite este: {lista_elemente_inmultite}")
suma = sum(lista_elemente_inmultite)
rest = suma % 11

print(f'Suma este {suma}. Restul impartirii sumei la 11 este {rest} si cifra de control este {lista_cnp_de_analizat[12]}')
if rest == 10 and lista_cnp_de_analizat[12] == 1:
    print("CNP VALID!")
elif rest == lista_cnp_de_analizat[12]:
    print("CNP VALID!")
else:
    print("CNP INVALID")
