# kysyy lukuja siihen saakka kunnes syöttää
# tyhjän merkkijonon. Lopuksi tulostaa saaduista luvuista
# viisi suurinta suurimmasta alkaen.
# Vinkki sort-metodi reverse=True

numbers = []
while True:
    user_input = input("Syötä numero (tai paina Enter lopettaaksesi): ")
    if user_input == "":
        break

    try:
        luku = int(user_input)
        numbers.append(luku)
    except ValueError:
        print("Virheellinen syöte. Syötä luku.")

if len(numbers) >= 5:
    numbers.sort(reverse=True)

    print("Viisi suurinta lukua ovat (suurimmasta pienimpään): ")
    for i in range(5):
        print(numbers[i])

else:
    print("Et syöttänyt tarpeeksi numeroita.")