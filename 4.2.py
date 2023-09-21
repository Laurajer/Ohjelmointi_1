#muuntaa tuumia senttimetreiksi niin kauan
# kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.

tuumat = float(input('Anna tuumat: '))

while 0 <= tuumat:
    sentit = tuumat * 2.54
    print(sentit)
    tuumat = float(input('Anna tuumat: '))

print('Annoit negatiivisen arvon.')