airport_data = {}

def add_airport():
    icao_code = input("Anna lentäkentän ICAO koodi: ")
    airport_nimi = input("Anna lentokentän nimi: ")
    airport_data[icao_code] = airport_nimi
    print(f"Lentokentän ICAO koodi {icao_code} ja nimi '{airport_nimi}' lisätty.")

def hae_airport():
    icao_code = input("Syötä halutun lentäkentän ICAO koodi: ")
    airport_nimi = airport_data.get(icao_code)
    if airport_nimi:
        print(f"Lentokenttä ICAO koodilla {icao_code} on '{airport_nimi}'.")
    else:
        print(f"Ei löytynyt kyseistä koodia {icao_code}.")


while True:
    print("Vaihtoehdot:")
    print("1. Lisää lentokenttä")
    print("2. Hae lentokentän tiedot")
    print("3. Lopeta")

    choice = input("Anna vaihtoehto (1/2/3): ")

    if choice == "1":
        add_airport()
    elif choice == "2":
        hae_airport()
    elif choice == "3":
        print("Hei hei!")
        break
    else:
        print("Virheellinen valinta. Syötä 1, 2 tai 3.")