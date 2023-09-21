#import random

#noppien_maara = int(input('Anna noppien lukumäärä: '))
#yhteensa = int(noppien_maara) * (random.randint(1, 6))
#print('Silmälukujen summa on: ' + str(yhteensa))

#MISSÄ FOR????

import random

noppien_maara = int(input("Anna noppien lukumäärä: "))
yhteensa = 0

for i in range(noppien_maara):
    nopan_silmaluku = random.randint(1,6)
    yhteensa += nopan_silmaluku

print("Silmälukujen summa on: ", yhteensa)