vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")

kuukauden_numero = int(input("Anna kuukausi numerona (1-12): "))

if 1 <= kuukauden_numero <= 12:
    kausi_numerona = (kuukauden_numero % 12) // 3
    vuodenajat = vuodenajat[kausi_numerona]
    print(f"Vuodenaika kuukaudelle {kuukauden_numero} on {vuodenajat}.")
else:
    print("Virheellinen syöte. Anna numero 1-12.")