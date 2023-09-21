luku_str = (input('anna luku: '))
kerrat = 0

while not len(luku_str) == (0):
    luku_int = int(luku_str)
    if kerrat == 0:
        suurin_luku = luku_int
        pienin_luku = luku_int
    else:
        if suurin_luku < luku_int:
            suurin_luku = luku_int
        elif pienin_luku > luku_int:
            pienin_luku = luku_int
    luku_str = (input('Anna luku: '))
    kerrat = 1

    print(f'Suurin luku oli {suurin_luku} ja pienin luku oli {pienin_luku}.')