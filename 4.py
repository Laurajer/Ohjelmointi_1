import random

noppa1 = noppa2 = heitot = 0
while (noppa1==6 or noppa2==6):
    noppa1 = random.randint()
    noppa2 = random.randint
    heitot = heitot + 1
print(f'Tarvittiin {heitot:d} heittoa.')