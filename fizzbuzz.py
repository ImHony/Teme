limita = input("Introdu limita superioara: ")

for numar in range(1, int(limita) + 1):
    if numar % 3 == 0 and numar % 5 == 0:
        print(f"{numar} FizzBuzz")
    elif numar % 3 == 0:
        print(f"{numar} Fizz")
    elif numar % 5 == 0:
        print(f"{numar} Buzz")
    else:
        print(numar)
