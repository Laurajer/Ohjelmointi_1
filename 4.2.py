#muuntaa tuumia senttimetreiksi niin kauan
# kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.

tuuma = int(input('Anna tuumamäärä: '))
sentit = float(tuuma) * 2.54

while int(tuuma) >= 0:
    if int(tuuma) < 0:
        break
    print(sentit)
    tuuma = int(input('Anna tuumamäärä:'))

print('Ei sallittu')