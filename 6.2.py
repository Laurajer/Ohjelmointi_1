import random

def heita_noppa(tahkot):
    return random.randint(1, tahkot)

max_numero = int(input("Anna nopan maksimi numero: "))

while True:
    result = heita_noppa(max_numero)
    print("Nopan silmäluku: ", result)

    if result == max_numero:
        print("Sait maksiminumeron! Voitit!")
        break