#koodi kysyy käyttäjätunnuksen ja salasanan
# tunnus : python
# Salasana : rules

SALASANA = ('rules')
TUNNUS = ('python')
salasana = tunnus = 0

while (salasana != SALASANA or tunnus != TUNNUS):
    tunnus = input('Anna käyttäjätunnus: ')
    salasana = input('Anna salasana: ')
    if tunnus != TUNNUS or salasana != SALASANA:
        print('Pääsy evätty!')
    else:
        print('Tervetuloa!')