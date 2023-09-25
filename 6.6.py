import math


def yksikko_hinta(halkaisija, hinta):
    radius = halkaisija / 2
    pizzan_pinta_ala = math.pi * (radius ** 2)
    pizzan_pinta_ala = hinta / (pizzan_pinta_ala / 10_000)
    return pizzan_pinta_ala


ekapizza_halkaisija = float(input("Anna 1. pizzan halkaisija cm: "))
tokapizza_halkaisija = float(input("Anna 2. pizzan halkaisija cm: "))
eph = float(input("Anna 1. pizzan hinta: "))
tph = float(input("Anna 2. pizzan hinta: "))

eka_yksikkohinta = yksikko_hinta(ekapizza_halkaisija, eph)
toka_yksikkohinta = yksikko_hinta(tokapizza_halkaisija, tph)
if eka_yksikkohinta < toka_yksikkohinta:
    print("Eka parempi, nom nom.")
elif toka_yksikkohinta < eka_yksikkohinta:
    print("Toka on nom nom.")
else:
    print("Nom nom molemmat.")