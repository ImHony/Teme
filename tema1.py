
# EX 1
sir = input("Introdu un sir: ")

if sir.isalpha():
    print(f"Sirul de caractere a fost gasit de {sir}")
elif sir.isdigit():
    print("Sirul este format doar din cifre")
elif sir.isalpha() or sir.isalnum():
    print("Sirul este format din mai multe tipuri de carcatere")

# EX 2

numar = input("Introdu un numar: ")
print("Par" if int(numar) % 2 == 0 else "Impar")

# EX 3

an = input("Introdu anul: ")
print("An bisect" if int(an) % 4 == 0 else "Anul nu este bisect")

# EX 4

alt_numar = input("Introdu un numar: ")

if int(alt_numar) > 0 and int(alt_numar) < 10:
    print("Numarul este pozitiv si mai mic decat 10.")
elif int(alt_numar) < 0:
   conversie_pozitiv = int(alt_numar) * - 1
   print(f"{conversie_pozitiv} este pozitiv.")
elif int(alt_numar) == 0:
    print("Numarul este 0")

# EX 5
print("1 – Afisare lista de cumparaturi \n2 – Adaugare element\n3 – Stergere element\n4 – Stergere lista de cumparaturi\n5 - Cautare in lista de cumparaturi ")
meniu = input("Introdu operatia dorita: ")
alegere = int(meniu)

if alegere == 1:
    print("Afisare lista de cumparaturi")
elif alegere == 2:
    print("Adaugare element")
elif alegere == 3:
    print("Sterere element")
elif alegere == 4:
    print("Sterge lista de cumparaturi")
elif alegere == 5:
    print("Cautare in lista de cumparaturi")
else:
    print("Alegerea nu exista.")