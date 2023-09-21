kaupungit = []

for i in range(5):
    kaupunki = input(f"Anna kaupungin nimi #{i + 1}: ")
    kaupungit.append(kaupunki)
print("Syötetyt kaupungit: ")
for kaupunki in kaupungit:
    print(kaupunki)