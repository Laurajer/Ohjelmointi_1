nimet_set = set()

while True:
    nimi = input("Anna nimi (tai paina Enter lopettaaksesi): ")
    if nimi == "":
        break

    if nimi in nimet_set:
        print("Jo listassa.")
    else:
        print("Uusi nimi")

    nimet_set.add(nimi)

print("Lista nimistä jotka syötettiin: ")
for nimi in nimet_set:
    print(nimi)