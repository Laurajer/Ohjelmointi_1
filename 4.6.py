#Koodin tarkoitus on määrittää piin likiarvo
import random

TOISTOT = 1000000
kerrat = 0
sisalla = 0

while TOISTOT > kerrat:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if pow(x, 2) + pow(y, 2) < 1:
        sisalla += 1
    kerrat += 1

print((4 * sisalla) / TOISTOT)