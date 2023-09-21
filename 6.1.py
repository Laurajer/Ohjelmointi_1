import random

def heita_noppa():
    return random.randint(1,6)

while True:
    result = heita_noppa()
    print("Nopan silmäluku: ", result)

    if result == 6:
        print("Sait kuutosen! Voitit!")
        break